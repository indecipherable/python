import numpy as np

arr = np.random.randn(6,3)
print(arr)
print("np.dot(arr.T,arr) - computer inner matrix product")
print(np.dot(arr.T,arr))
