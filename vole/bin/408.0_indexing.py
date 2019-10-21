import numpy as np

arr = np.empty((8,4))
for i in range(8):
  arr[i] = i
print(arr)

print(arr[[4,3,0,6]])
