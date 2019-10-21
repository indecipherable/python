import numpy as np

arr = np.empty((8,4))
for i in range(8):
  arr[i] = i

arr = np.arange(32).reshape((8,4))
print(arr)
print("")

arr = np.arange(32).reshape((4,8))
print(arr)
print("")
