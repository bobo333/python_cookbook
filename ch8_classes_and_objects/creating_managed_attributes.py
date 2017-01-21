# add type checking or validation to the getting and setting of an attributes
# use properties
import math


class Person:
    def __init__(self, first_name):
        self._first_name = None     # define it first here so pycharm doesn't complain
        self.first_name = first_name

    # Getter fxn
    @property
    def first_name(self):
        return self._first_name

    # Setter fxn
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string for first_name')
        self._first_name = value

    # Deleter fxn
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attributes")


a = Person('Guido')
print(a.first_name)     # calls getter
a.first_name = 'Paul'   # calls the setter
print(a.first_name)

try:
    a.first_name = 55
except TypeError:
    print('type error')

try:
    del a.first_name
except AttributeError:
    print('Attribute error')


print('\n'*2)


# can also use properties can be defined for existing get and set methods


class Person2:
    def __init__(self, first_name):
        self._first_name = None     # set here so PEP8 doesn't complain
        self.set_first_name(first_name)

    # getter fxn
    def get_first_name(self):
        return self._first_name

    # setter fxn
    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected string for first_name')
        self._first_name = value

    # Deleter fxn (optional)
    def del_first_name(self):
        raise AttributeError('Can not delete attribute')

    # Make a property from existing get/set methods
    first_name = property(get_first_name, set_first_name, del_first_name)


person2 = Person('John')
# properties are methods bundled together. There are raw fget, fset, and fdel properties
print(Person2.first_name.fget)
print(Person2.first_name.fset)
print(Person2.first_name.fdel)

# properties should only be used when it adds extra functionality, like validation
# don't follow java-like standards where everything uses getters and setters
print()

# properties can also be computed on demand, instead of returning stored values
# ex:


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

c = Circle(4.0)
print(c.radius)
print(c.area)
print(c.perimeter)

# in general, repetitive property methods should be avoided, it leads to bloated code and there are better patterns
# available
