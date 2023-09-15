#Generate Random Number
#NumPy offers the random module to work with random numbers.

#Generate a random integer from 0 to 100
from numpy import random

x = random.randint(100)

print(x)

#Generate Random Float
#Generate a random float from 0 to 1

x = random.rand()

print(x)

#Generate Random Array
#Generate a 1-D array containing 5 random integers from 0 to 100

x=random.randint(100, size=(5))

print(x)

#Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100

x = random.randint(100, size=(3, 5))

print(x)

#Generate a 1-D array containing 5 random floats\

x = random.rand(5)

print(x)

#Generate a 2-D array with 3 rows, each row containing 5 random numbers

x = random.rand(3, 5)

print(x)

#Generate Random Number From Array

#Return one of the values in an array

x = random.choice([3, 5, 7, 9])

print(x)

#Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9)

x = random.choice([3, 5, 7, 9], size=(3, 5))

print(x)