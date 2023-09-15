#Create Your Own ufunc

#Create your own ufunc for addition:

import numpy as np

def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

#Check if a Function is a ufunc

print(type(np.add))

#Check the type of another function: concatenate():

print(type(np.concatenate))

#Check the type of something that does not exist. This will produce an error:

print(type(np.blahblah))

#Use an if statement to check if the function is a ufunc or not:

if type(np.add) == np.ufunc:
  print('add is ufunc')
else:
  print('add is not ufunc')
  