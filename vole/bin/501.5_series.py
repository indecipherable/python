import pandas
import numpy
from pandas import Series, DataFrame

obj2 = pandas.Series([4,7,-5,3], index=['d','b','a','c'])

print("obj2 > 0:")
print(obj2[obj2 > 0])

print("obj2 * 2:")
print(obj2 * 2)

print("numpy.exp(obj2):")
print(numpy.exp(obj2))
