import numpy as np
import numpy.linalg

# numpy to the rescue again
m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
print(m)
print()

# transpose
print(m.T)
print()

# inverse
print(m.I)
print()

# create a vector and multiply
v = np.matrix([[2], [3], [4]])
print(v)
print(m * v)
print()

# more in numpy.linalg
print(numpy.linalg.det(m))
print()

# eigenvalues
print(numpy.linalg.eigvals(m))
print()

# solve for x in mx = v
x = numpy.linalg.solve(m, v)
print(x)
print(m * x)
print(v)
