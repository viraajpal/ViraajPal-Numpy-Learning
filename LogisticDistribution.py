#Logistic Distribution

#Draw 2x3 samples from a logistic distribution with mean at 1 and stddev 2.0

from numpy import random

x = random.logistic(loc=1, scale=2, size=(2, 3))

print(x)

#Visualization of Logistic Distribution

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.logistic(size=1000), hist=False)

plt.show()

#Difference Between Logistic and Normal Distribution


sns.distplot(random.normal(scale=2, size=1000), hist=False, label='normal')
sns.distplot(random.logistic(size=1000), hist=False, label='logistic')

plt.show()