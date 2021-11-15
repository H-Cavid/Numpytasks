# import  numpy as np
# array = np.array(np.random.randint(3,10,15))#3-den 10-a kimi 15dene random eded verir
# array.shape = (3,5)

# array2 = np.array(np.random.randint(2,24,5))
# array2.shape = (1,5)
# #broadcastda olmuyan setri tekrar gotrur
# array3 = array2+array
# array3 = array +5
# # print(array3)
# # print(array)
# # print(array.shape)
# # print(array2)
# # print(array2.shape)

# # resize birbasa arrayi cevirir reshape ise yox

# array6=array.max(axis=0)
# print(array6)

from numpy.random.mtrand import exponential,standard_exponential,standard_normal
import pandas as pd
import numpy as np
import math



np_arr = np.random.randn(6,5)

arr = (np_arr -np_arr.mean())/np_arr.std()

def distr(x):
    return 1/math.sqrt(2*3.14)*math.exp(-x*x/2)

def f(x):
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i,j]=distr(x[i,j])
    return x

print(np_arr)
print(f(np_arr))
#print(arr)




















