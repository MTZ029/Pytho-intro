print("This is Talha")
import matplotlib

print(matplotlib.__version__)  # simple 

import matplotlib.pyplot as plt

import seaborn as sns

from numpy import random

sns.distplot([0,1,2,3,4,5])

#plt.show()

sns.distplot([5,6,7,8,9,10,11,12,13,14,15])
# plt.show()

sns.distplot([1,2,5,6,7,8,9],hist=False)
# plt.show()

sns.distplot(random.normal(size=99),hist=False)
#plt.show()

x =random.binomial(n=5 , p=0.5 , size=(5))
print(x)  # simply prints the elements that are from the array understudy

sns.distplot(random.normal(loc=50 , scale= 5 ,size =1000),hist=False ,label='Normal')
sns.distplot(random.binomial(n=100 , p=0.5 , size=1000),hist=False ,label='Binomial')
plt.show()