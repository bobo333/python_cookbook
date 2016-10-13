from itertools import chain

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

for x in chain(a, b):
    print(x)

# this is more efficient than combining them first, as that requires them to be the same type and makes a new sequence
