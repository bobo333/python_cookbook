import math

# read-only attribute that is only computed when first accessed, and then it is cached


class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius


c = Circle(4.0)
print(c.radius)
print(c.area)
print(c.area)
print(c.perimeter)
print(c.perimeter)
print()


# this works because if a descriptor only defines __get__, the __get__ method only fires if the attribute being accessed
# isn't in the underlying instance dictionary __dict__

c2 = Circle(2.0)
print(vars(c2))
print(c2.area)
print(vars(c2))
print(c2.area)  # calculation not triggered
print()

del c2.area
print(vars(c2))
print(c2.area)
print()


# computer value does become mutable though, can overcome this with a slightly less efficient implementation
c2.area = 99


def laziestproperty(func):
    name = '_lazy_' + func.__name__

    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            value = func(self)
            setattr(self, name, value)
            return value

    return lazy


class BetterCircle:
    def __init__(self, radius):
        self.radius = radius

    @laziestproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @laziestproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius


bc = BetterCircle(4.0)
print(bc.area)


try:
    bc.area = 99
except AttributeError:
    print('attribute error dude!')
