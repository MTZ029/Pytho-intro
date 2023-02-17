print("This is the code of practice program of the grapgh")


"""
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n=100 , p=0.5 ,size=1000),hist=False , label='binomial')

plt.show()

sns.distplot(random.poisson(lam =10 , size=10000),kde=True,hist=False ,label='Hyundai')
plt.show()

sns.distplot(random.uniform(size=100000),hist=False)
plt.show()    """

import numpy as np
from numpy import random
import matplotlib.pyplot as plt 
import seaborn as sns

sns.distplot(random.normal(loc=2 , scale= 5 , size= 200),hist=False,label='Normal')
sns.distplot(random.binomial(n=5 , p=0.5 , size=400),hist=False ,label='Binomial')
sns.distplot(random.poisson(lam=10 ,size=1000), hist=False , label='Poisson')
sns.distplot(random.uniform(size=2000),hist=False ,label='Uniform')
sns.distplot(random.logistic(size=10000),hist=False, kde=True , label='Logistic')
sns.distplot(random.multinomial(n=8,pvals=[1/8,1/8,1/8,1/8,1/8,1/8,1/8,1/8]),hist=False ,label='Multinomial')
sns.distplot(random.exponential(size=10000),hist=False ,label='Exponential') #The value of scale =1.0 by default
plt.show()


