#Zipf Distribution

#Draw out a sample for zipf distribution with distribution parameter 2 with size 2x3

from numpy import random

x = random.zipf(a=2, size=(2, 3))

print(x)

#Visualization of Zipf Distribution

import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=2, size=1000)
sns.distplot(x[x<10], kde=False)

plt.show()


# import numpy as np
#
# var = np.array([[1, 2], [2, 2]])
# print(var.shape)