import pandas
import numpy
from pandas import Series, DataFrame

obj2 = pandas.Series([4,7,-5,3], index=['d','b','a','c'])

print("'b' in obj2:")
print('b' in obj2)
print("'e' in obj2:")
print('e' in obj2)
