# define the __str__() and __repr__()
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r}'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


# repr is what's printed out on the command line to inspect a variable
# str is what's given when print(variable) is called
# the 0.x means to use the x attribute of the 0 argument to format(), which in this case is self.x
# if no __str__ exists, __repr__ is used as a fallback

p = Pair(3, 4)
print('p is {0!r}'.format(p))   # the !r means to use the __repr__
print('p is {0}'.format(p))     # __str__ is the default
print()

# it is standard practice for eval(repr(x)) == x, if this isn't possible, a useful text representation enclosed in < >
# is preferred
f = open('data/file.dat')
print('{0!r}'.format(f))
