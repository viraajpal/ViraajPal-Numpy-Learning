#Shuffling Arrays

#Randomly shuffle elements of following array

from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)

print(arr)
print()

#Generating Permutation of Arrays


arr = np.array([1, 2, 3, 4, 5])

print(random.permutation(arr))

