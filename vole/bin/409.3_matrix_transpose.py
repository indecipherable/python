import numpy as np

arr = np.arange(16).reshape((2,2,4))
print(arr)
print(arr.swapaxes(1,2))
print(arr.swapaxes(0,2))
