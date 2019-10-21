import pandas
from pandas import Series, DataFrame

obj2 = pandas.Series([4,7,-5,3], index=['d','b','a','c'])

print(obj2)

print("obj2['a']:")
print(obj2['a'])
print("assigning 'd' = 6")
obj2['d'] = 6

print(obj2)
