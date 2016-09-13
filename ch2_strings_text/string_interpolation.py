import sys
import string

s = '{name} has {n} messages'
print(s.format(name='Steve', n=999))


# can use format_map() plus vars()
name = 'Steve'
n = 999

print(s.format_map(vars()))


# vars() also works with instances
class Info(object):
    def __init__(self, name, n):
        self.name = name
        self.n = n

a = Info('Bob', 9999)
print(s.format_map(vars(a)))


# dealing with missing values
try:
    s.format(name='Joe')
except KeyError:
    print('KeyError')


class SafeSub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

del n
print(s.format_map(SafeSub(vars())))
print()


# another option
def sub(text):
    return text.format_map(SafeSub(sys._getframe(1).f_locals))

name = 'Joe'
n = 42

print(sub('You have {n} messages.'))
print(sub('Hello {name}'))


# can also do this, but it's not preferred, .format() has much more functionality
temp = string.Template('$name has $n messages')
print(temp.substitute(vars()))
