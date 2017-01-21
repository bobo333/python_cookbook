# want to encapsulate "private" data in instances of a class, but python doesn't have access control
# in lieu of actual access control, naming conventions are used to indicate privacy


class A:
    def __init__(self):
        self._internal = 0  # an internal attributes
        self.public = 1     # a public attributes

    def public_method(self):
        """
        A public method
        """
        print(self.public)

    def _internal_method(self):
        """
        A ninternal method
        """
        print(self._internal)


a = A()

a.public_method()
a._internal_method()    # can still access internal methods, but can result in brittle code, use caution
print()

# double underscores causes the name to be mangled. ex:


class B:
    def __init__(self):
        self.__private = 0          # will actually be _B__private

    def __private_method(self):     # will actually be _B__private_method
        print(self.__private)

    def public_method(self):
        self.__private_method()


b = B()
b.public_method()
try:
    b.__private_method()
except AttributeError:
    print('Attribute error')

b._B__private_method()


# mangling makes it so such attributes can not be overridden via inheritance. ex:
class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1      # does not override B.__private

    def __private_method(self):
        print(self.__private)


c = C()
c._C__private_method()
c._B__private_method()

# generally only use double underscore if you're intentionally hiding it from sub-classes

# if naming something and need to avoid conflict with keywords, use a trailing underscore:
lambda_ = 2.0   # trailing _ to avoid clash with lambda keyword
