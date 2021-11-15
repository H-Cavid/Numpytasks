import numpy as np

# arr = np.array(np.random.randint(20,50,30))#20-50 arasinda 30 random eded verecek


# arr1=arr[np.newaxis:,]

# arr2=arr.reshape(5,6)
# arr3=arr2[:,3]
# print(arr2)
# print(arr3)
#newaxis vektora cevirir
np.random.seed(10)#eyni baslangicdan elemek ucun
gardes=np.array(np.random.randint(50,100,20))
# print(gardes)
grades_20 =np.round(gardes/5)#round tam ededlerin tam hissesini gosterir
# grades_20 =grades_20.reshape(4,5)
# grades_20=grades_20[:2,:]
# grades_20=grades_20[1:3,2:4]
# grades_20=grades_20.max()
# grades_20=grades_20.mean()
# grades_20=grades_20.std()
# print(dir(grades_20))
# print(grades_20)
# print(grades_20.shape)


positions = np.array(['C','M','P','M','C','P','G','G','M'])
print(positions)
height = np.array([1.73,1.82,1.65,1.70,1.85,1.77,1.56,1.72,1.69])
print(height)
print(height[positions=='C'].mean())






# arr2=arr[:,np.newaxis]
# print(arr2)
# print(arr1.shape)
# print(arr2.shape)
# [row,col]