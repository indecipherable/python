import numpy as np

arr = np.random.randn(7) * 5
print(arr)
print("")
remainder, whole_part = np.modf(arr)
print("remainder is:")
print(remainder)
print("")
print("whole part is:")
print(whole_part)
print("")
print("numpy.sqrt(arr) is:")
print(np.sqrt(arr))
print("")
print("numpy.sqrt(arr, arr)")
print("")
print(np.sqrt(arr,arr))
