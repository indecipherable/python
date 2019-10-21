import numpy as np 

array1 = np.array([[1., 2., 3.], [4., 5., 6.]])
array2 = np.array([[10., 20., 30.], [40., 50., 60.]])
array3 = np.arange(15)
array_slice1=array1[2:6]
array_slice2=array2[2:6]
array_slice3=array3[2:6]
print(array_slice1)
print(array_slice2)
print(array_slice3)
#array_slice1[1] = 1234
#array_slice2[1] = 1234
array_slice3[1] = 1234
#print(array_slice1)
#print(array_slice2)
print(array_slice3)
array_slice3[:] = 345
print(array_slice3)
print(array3)
