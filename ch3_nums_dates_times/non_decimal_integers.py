x = 1234
print(bin(x))
print(oct(x))
print(hex(x))
print()

# using format will remove the leading 0b, 0o, and 0x
print(format(x, 'b'))
print(format(x, 'o'))
print(format(x, 'x'))
print()
y = -1234
print(format(y, 'b'))
print(format(y, 'o'))
print(format(y, 'x'))

# to get an unsigned value from a negative one, add the max value to set the bit length
print(format(2**32 + y, 'b'))
print(format(2**32 + y, 'x'))
print()

# to convert integer strings in different bases, use the int() fxn with the appropriate base
print(int('4d2', 16))
print(int('10011010010', 2))
