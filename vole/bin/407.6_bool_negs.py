import numpy as np
import numpy.random #as rnd

names = np.array(['Bushmaster','Mariah','Misty','Luke','Styler0','Styler1','Styler2'])
#print(names == 'Luke')
data = np.random.randn(7,4)

mask = (names == 'Mariah') | (names == 'Misty')

#print(mask)
#print(data[mask])

mask2 = (names == 'Bushmaster') & (names == 'Styler0')

#print(mask2)
#print(data[mask])

data[data < 0] = 0
print(data)
