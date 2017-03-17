# super is used to call methods on a parent class
# often used in the __init__ fxn


class A:
    def __init__(self):
        self.x = 0

    def spam(self):
        print('A.spam')


class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1

    def spam(self):
        print('B.spam')
        super().spam()      # call parent spam


b = B()
b.spam()
print()


# also used when overriding special methods
class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # delegate attribute lookup to internal obj
    def __getattr__(self, name):
        return getattr(self._obj, name)

    # delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)    # call original __setattr__
        else:
            setattr(self._obj, name, value)


# not using super can get strange, then again, so can inheritance in general
class Base:
    def __init__(self):
        print('Base.__init__')


class A(Base):
    def __init__(self):
        Base.__init__(self)
        print('A.__init__')


class B(Base):
    def __init__(self):
        Base.__init__(self)
        print('B.__init__')


class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print('C.__init__')


c = C()     # Base.__init__ called twice
print()


# using super eliminates this because of MRO (method resolution order) This is often challenging to understand
class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')


class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')


class C(A, B):
    def __init__(self):
        super().__init__()  # only one call to super here
        print('C.__init__')


c = C()
print(C.__mro__)
