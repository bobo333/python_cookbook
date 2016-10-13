from itertools import zip_longest


xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]

for x, y in zip(xpts, ypts):
    print(x, y)
print()

# zip produces an iterator of tuples, it ends when the shortest input sequence is exhausted
xvals = ['a', 'b', 'c']
yvals = [1, 2, 3, 4, 5, 6]
for x, y in zip(xvals, yvals):
    print(x, y)
print()

# to stop on the longest instead of shortest, zip_longest can be used
for x, y in zip_longest(xvals, yvals):
    print(x, y)
print()

# a fill value can be given in place of None as well
for x, y in zip_longest(xvals, yvals, fillvalue='HI'):
    print(x, y)
print()

# it can take more than 2 sequences as well
first = [1, 2, 3, 4]
second = [11, 22, 33, 44]
third = [111, 222, 333, 444]

for x, y, z in zip(first, second, third):
    print(x, y, z)
print()

# zip returns an iterator, use list() if you need all the items at once
