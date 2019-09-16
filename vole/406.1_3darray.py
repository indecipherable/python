import numpy as np

array3d1 = np.array([[[1, 2, 3],[4, 5, 6]], [[7, 8, 9],[10, 11, 12]]])
array3d1_old = array3d1[0].copy()
array3d1[0] = 42
print(array3d1)
array3d1[0] = array3d1_old
print(array3d1)
