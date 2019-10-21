import numpy as np

arr = np.empty((8,4))
for i in range(8):
  arr[i] = i

arr = np.arange(32).reshape((8,4))
# select subset of matrix rows and columns
print(arr[[1,5,7,2]][:, [0,3,1,2]])
