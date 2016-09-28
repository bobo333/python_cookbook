from fractions import Fraction

a = Fraction(5, 4)
b = Fraction(7, 16)
print(a + b)
print(a * b)
print()

# getting numerator and denominator
c = a * b
print(c.numerator)
print(c.denominator)
print()

# convert to float
print(float(c))
print()

# limit denominator finds the closest fraction with a denominator equal to or smaller than the specified number
x = Fraction('3.1415926535897932')
print(x.limit_denominator(100))

y = Fraction(311, 99)
print(float(y))
print()

# convert float to fraction
x = 3.75
y = Fraction(*x.as_integer_ratio())
print(y)
