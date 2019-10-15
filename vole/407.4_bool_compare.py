import numpy as np
import numpy.random #as rnd

names = np.array(['Bushmaster','Mariah','Misty','Luke','Styler0','Styler1','Styler2'])
print(names == 'Luke')
data = np.random.randn(7,4)
# invert the condition
cond = names == 'Luke'
print(data[~cond])
# print non-inverted
print(data[cond])
