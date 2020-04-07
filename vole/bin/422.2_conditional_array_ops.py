import numpy as np

arr = np.random.randn(4, 4)
print "array is: \n%r" % arr

evalarrgt0 = arr > 0
print "arr gt 0: \n%r" % evalarrgt0

evalarrlt0 = np.where(arr < 0, 0, arr) # set negative values to 0
print "arr lt 0 eq 0: \n%r" % evalarrlt0

#result = [(x if c else y)
#  for x, y, c in zip(xarr, yarr, cond)]

#print result
