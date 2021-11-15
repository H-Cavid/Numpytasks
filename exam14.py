import numpy as np
from numpy import random,size
from numpy.core.fromnumeric import shape
a=np.random.randint(7,34,size=(3,2,5))#3dene 2nin 5-e matris yaradir
print(a)
print(a.shape)
print(a.ndim)
# b=np.random.randint(size=(3,2,5),range=(7,34)) 
# c=np.random.randint(7,34,shape(3,2,5))
# print(c)

