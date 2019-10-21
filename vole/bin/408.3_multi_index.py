import numpy as np

arr = np.empty((8,4))
for i in range(8):
  arr[i] = i

arr = np.arange(32).reshape((8,4))
#print(arr)
print(arr[[0,2,4,6],[1,3,2,0]])
print("")
arr = np.arange(32).reshape((4,8))
#print(arr)
print(arr[[0,1,2,3],[1,3,5,7]])
print("")
