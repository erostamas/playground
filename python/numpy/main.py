import numpy

arr = numpy.array([1,2,3,4,5,6,7,8,9])
arr2 = arr * 10
print(arr2)

mat = numpy.array([[1,2,3,4,5],[6,7,8,9,10]])
print(mat)

# Matrix multiplication
result = np.dot(mat, np.array([5, 6]))
print(result)  # [17 39]

# Element-wise math
print(np.sqrt(arr))  # [1.         1.41421356 1.73205081 2.         2.23606798]

#How is NumPy different from pandas?
#NumPy focuses on numerical arrays and mathematical operations.

#Pandas builds on NumPy and adds labels, heterogeneous data types, and table-like data structures.