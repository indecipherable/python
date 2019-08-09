import pandas
from pandas import Series, DataFrame

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
# cast dict as Series
obj3 = pandas.Series(sdata)

print(obj3)
