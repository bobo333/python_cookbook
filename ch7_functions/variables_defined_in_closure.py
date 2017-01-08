import sys
from timeit import timeit


# can attach accessor methods to the closure function to get at variables inside the closure
def sample():
    n = 0

    # closure function
    def func():
        print('n = ', n)

    # accessor methods for n
    def get_n():
        return n

    def set_n(value):
        nonlocal n  # nonlocal allows modification of inner variables
        n = value

    # attach as function attributes
    func.get_n = get_n
    func.set_n = set_n
    return func


f = sample()
f()

f.set_n(10)
f()

print(f.get_n())
print()

# can do something similar where closures emulate instances of a class
class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals

        # update instance dictionary with callables
        self.__dict__.update((key, value) for key, value in locals.items() if callable(value))

    # redirect special methods
    def __len__(self):
        return self.__dict__['__len__']()


# example use:
def Stack():
    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()


s = Stack()
print(s)
s.push(10)
s.push(20)
s.push('Hello')
print(len(s))
print(s.pop())
print(s.pop())
print(len(s))
print()


# this is more performant than a normal class definition
class Stack2:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)


s = Stack()
print(timeit('s.push(1);s.pop()', 'from __main__ import s'))
s2 = Stack2()
print(timeit('s2.push(1);s2.pop()', 'from __main__ import s2'))
