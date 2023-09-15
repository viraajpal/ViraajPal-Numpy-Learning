# elements from index 1 to index 5 from the following array

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])

#elements from index 4 to the end of the array

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[4:])

#elements from the beginning to index 4 (not included

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[:4])

#the minus operator to refer to an index from the end

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])
#step value to determine the step of the slicing

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])

#every other element from the entire array

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[::2])

# the second element, slice elements from index 1 to index 4 (not included)

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])

# both elements, return index 2

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 2])

# both elements, slice index 1 to index 4 (not included), this will return a 2-D array

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 1:4])

