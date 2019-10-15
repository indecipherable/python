import numpy as np
import numpy.random #as rnd

names = np.array(['Bushmaster','Mariah','Misty','Luke','Styler0','Styler1','Styler2'])
print(names == 'Luke')
data = np.random.randn(7,4)
# pass boolean array when indexing
print(data[names=='Luke'])
# select from rows where names == 'Luke'
print(data[names == 'Luke', 2:])
# index columns
print(data[names == 'Luke', 3])
