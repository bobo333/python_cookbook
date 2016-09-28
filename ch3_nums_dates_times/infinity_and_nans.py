import math

inf = float('inf')
neg_inf = float('-inf')
nan = float('nan')

print(inf)
print(neg_inf)
print(nan)

print()

print(math.isinf(inf))
print(math.isnan(nan))

print()

# infinity and negative infinity will propagate through calculations
print(inf + 45)
print(neg_inf + 45)
print(inf * 45)
print(10 / neg_inf)
print(10 / inf)
print()

# however, some things result in NaN instead
print(10 / nan)
print(inf / inf)
print(inf + neg_inf)
print()

# NaN propagates through operations without throwing an exception
# the fpectl module can be used to make python throw exceptions for NaN, but this module is not enabled by default
print(nan + 23)
print(nan / 2)
print(nan * 2)
print(math.sqrt(nan))
print()

# NaN never compares as equal
a = float('nan')
b = float('nan')
print(a == b)
print(a is b)
print(a == a)   # not even equal to itself!

# because of that, the only way to check for NaN value is to use math.isnan()
