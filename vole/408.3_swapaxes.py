import numpy as np

arr = np.arange(16).reshape((2,2,4))
print(arr)
print("now swapaxes!!")
print(arr.swapaxes(1,2))
