# Accessing index

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])

#get third anf fourth index

arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3])

#Access 2-D array

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])

#2nd row, 5th column

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('5th element on 2nd row: ', arr[1, 4])

#Access 3-D Arrays------third element of the second array of the first array

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])


#negative index-- last element from the 2nd dim

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])