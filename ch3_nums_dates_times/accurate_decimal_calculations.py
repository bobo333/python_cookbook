from decimal import Decimal, localcontext
import math

# floating point numbers can't represent all base-10 decimal numbers correctly, even simple arithmetic can create errors
a = 4.2
b = 2.1

print(a + b)
print((a + b) == 6.3)   # False, wtf
print()

# can use the Decimal module for more accuracy, although with less performance
a = Decimal('4.2')
b = Decimal('2.1')
print(a + b)
print((a + b) == Decimal('6.3'))    # True
print()

# can control things about calculations with Decimal by creating a localcontext
a = Decimal('1.3')
b = Decimal('1.7')
print(a / b)

with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)

with localcontext() as ctx:
    ctx.prec = 50
    print(a / b)

# it's important to know when to use Decimal though, usually the small errors introduced by floats are fine and don't
# matter. Floats are also much faster than Decimal

# that being said, sometimes weird things happen when large and small numbers are added together, so be careful:
nums = [1.23e+18, 1, -1.23e+18]
print(sum(nums))    # prints 0.0 (the 1 disappears!)

# math.fsum will give a more accurate sum
print(math.fsum(nums))  # prints 1.0 as expected
