import numpy as np

arr = np.array([[0,1,2],[3,4,5],[6,7,8]])

print "array is: \n%r" %arr
print "array.sum() is: \n%r" %arr.sum()
print "array.sum(axis=1) is: \n%r" %arr.sum(axis=1)

print "array.mean() is: \n%r" %arr.mean()
print "array.mean(axis=1) is: \n%r" %arr.mean(axis=1)

print "array.std() is: \n%r" %arr.std()
print "array.std(axis=1) is: \n%r" %arr.std(axis=1)

print "array.var() is: \n%r" %arr.var()
print "array.var(axis=1) is: \n%r" %arr.var(axis=1)

print "array.min() is: \n%r" %arr.min()
print "array.min(axis=1) is: \n%r" %arr.min(axis=1)

print "array.max() is: \n%r" %arr.max()
print "array.max(axis=1) is: \n%r" %arr.max(axis=1)

print "array.argmin() is: \n%r" %arr.argmin()
print "array.argmin(axis=1) is: \n%r" %arr.argmin(axis=1)

print "array.argmax() is: \n%r" %arr.argmax()
print "array.argmax(axis=1) is: \n%r" %arr.argmax(axis=1)

print "array.cumsum() is: \n%r" %arr.cumsum()
print "array.cumsum(axis=1) is: \n%r" %arr.cumsum(axis=1)

print "array.cumprod() is: \n%r" %arr.cumprod()
print "array.cumprod(axis=1) is: \n%r" %arr.cumprod(axis=1)
