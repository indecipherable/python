import numpy as np

arr = np.array([ 0, 1, 2, 3, 4, 64, 64, 64, 8, 9])
arr2d0 = np.array([[ 0, 1, 2, 3],[ 4, 5, 6, 7],[ 8, 9, 10, 11],[ 12, 13, 14, 15]])
arr2d1 = np.array([[ 16, 17, 18, 19],[ 20, 21, 22, 23],[ 24, 25, 26, 27],[ 28, 29, 30, 31]])
arr2d2 = np.array([[ 32, 33, 34, 35],[ 36, 37, 38, 39],[ 40, 41, 42, 43],[ 44, 45, 46, 47]])
arr2d3 = np.array([[ 48, 49, 50, 51],[ 52, 53, 54, 55],[ 56, 57, 58, 59],[ 60, 61, 62, 63]])
print(arr2d0[:2])
print(arr2d1[1:3, 1:])
print(arr2d1[:4, 1:])
print(arr2d2)
print("arr3d[1:3] is:")
arr3d = np.array([[arr2d0],[arr2d1],[arr2d2],[arr2d3]])
print(arr3d[2:])
