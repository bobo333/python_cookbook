import cmath
import math

a = complex(2, 4)
b = 3 - 5j
print(a)
print(b)
print()

print(a.real)
print(a.imag)
print(a.conjugate())
print()

print(a + b)
print(a * b)
print(a / b)
print(abs(a))
print()

# more complex-valued functions are available in the cmath module
print(cmath.sin(a))
print(cmath.cos(a))
print(cmath.exp(a))
print()

# python's normal math functions do not produce complex numbers by default
try:
    print(math.sqrt(-1))
except ValueError:
    print("value error")

print(cmath.sqrt(-1))
