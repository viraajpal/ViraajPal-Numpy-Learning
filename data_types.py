#Checking the Data Type of an Array

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype)
#Creating Arrays With a Defined Data Type

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)

#For i, u, f, S and U we can define size as well

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)

#A non integer string like 'a' can not be converted to integer
arr = np.array(['a', '2', '3'], dtype='i')

#Converting Data Type on Existing Arrays

arr = np.array([1.1, 2.1, 3.1])

newarr1 = arr.astype('i')

print(newarr1)
print(newarr1.dtype)