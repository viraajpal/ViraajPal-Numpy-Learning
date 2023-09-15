# Create an array with its type

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))

#Use tuple to create an array



arr = np.array((1, 2, 3, 4, 5))

print(arr)
print(type(arr))

#0-D Arrays

arr = np.array(42)

print(arr)

#1-D Arrays


arr = np.array([1, 2, 3, 4, 5])

print(arr)


#2-D Arrays

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)

#3-D arrays

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)


# Check dimentios number



a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


#Check Higher dimension

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)