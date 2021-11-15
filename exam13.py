import numpy as np

arr1=np.arange(8).reshape(2,4)#0-dan 8 e qeder ededleri 2-nin 4-3 massive duzur
print(arr1)

arr2 = np.random.randint(1,10,8).reshape(2,4)#1-den 10-akimi 8  eded verir 1 massiv daxilinde onuda 2-nin 4e massive cevirir
print(arr2)

arr3=np.vstack([arr1,arr2])
print(arr3)

# arr4=np.hstack([arr1,arr2])
# print(arr4)