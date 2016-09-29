import numpy as np

# NumPy provides better performance and efficiency for mathematical computations than standard python lists

# normal python:
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

print(x * 2)

try:
    print(x + 10)
except TypeError:
    print("type error")

print(x + y)
print()

# numpy arrays
ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])
print(ax * 2)
print(ax + 10)
print(ax + ay)
print(ax * ay)
print()


def f(x):
    return 3 * x ** 2 - 2 * x + 7

print(f(ax))
print()

# numpy also provides a collection of "universal functions" that allow for array operations similar to those found in
# math module
print(np.sqrt(ax))
print(np.cos(ax))
print()

# numpy arrays are allocated similar to C or Fortran, they are large, contiguous memory regions consisting of a
# homogenous data type. This means they can be larger than anything normally put into a python list
grid = np.zeros(shape=(10000, 10000), dtype=float)
print(grid)
print()

# these still behave as expected with typical operations
grid += 10
print(grid)
print(np.sin(grid))
print()

# numpy extends python's list indexing, particularly with multi-dimensional arrays
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print()

# select row 1
print(a[1])
print()

# select column 1
print(a[:, 1])
print()

# select a subregion and change it
print(a[1:3, 1:3])
a[1:3, 1:3] += 10
print(a)
print()

# Broadcast a row vector across an operation on all rows
print(a + [100, 101, 102, 103])
print(a)
print()

# conditional assignment on an array
print(np.where(a < 10, a, 10))
