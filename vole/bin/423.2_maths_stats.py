import numpy as np

arr = np.random.randn(6,4)
print "got this 6x4 array: \n%r" %arr
print "arr.mean(axis=1) is:\n%r" %arr.mean(axis=1)
print "arr.mean(axis=0) is:\n%r" %arr.mean(axis=0)
print "arr.sum(axis=1) is:\n%r" %arr.sum(axis=1)
print "arr.sum(axis=0) is:\n%r" %arr.sum(axis=0)
