import numpy as np

arr = np.arange(16).reshape((2,2,4))
print(arr)
print("")
print(arr.transpose((1,0,2)))
print("")
print(arr.transpose((0,1,2)))
