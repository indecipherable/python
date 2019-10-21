import numpy as np

array_u8 = np.array([-2.68, -68.99, 1.01, 2.36, 3.333])
print(array_u8)
print(array_u8.dtype)
array_i8 = array_u8.astype(np.int64)
print(array_i8)
print(array_i8.dtype)
