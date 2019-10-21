import numpy as np

arr = np.empty((8,4))
for i in range(8):
  arr[i] = i

print(arr[[-3, -5, -7]])
