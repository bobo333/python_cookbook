text = 'Hello World!'

print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))
print()

print(text.ljust(20, '='))
print(text.rjust(20, '>'))
print(text.center(20, '_'))
print()

print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))
print()

print(format(text, '*>20'))
print(format(text, '=<20'))
print(format(text, '~^20'))
print()

# works with non-strings
print(format(55, '*>20'))
print(format(1.23, '=^10.2f'))
print()

# can use in .format() as well
print('{:>10s} {:>10s}'.format('Hello', 'World'))
