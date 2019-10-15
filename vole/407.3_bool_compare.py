import numpy as np
import numpy.random #as rnd

names = np.array(['Bushmaster','Mariah','Misty','Luke','Styler0','Styler1','Styler2'])
print(names == 'Luke')
data = np.random.randn(7,4)
# select everything but 'Luke'
print(names != 'Luke')
# negate the condition !=
print(data[~(names == 'Luke')])
