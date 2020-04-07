import numpy as np

xarr = np.array([1.1, 1.2, 1.3, 1.4])
yarr = np.array([2.1, 2.2, 2.3, 2.4])
cond = np.array([True, False, True, True])

result = [(x if c else y)
  for x, y, c in zip(xarr, yarr, cond)]

print result
