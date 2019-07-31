seq = [(1,2,3),(4,5,6),(7,8,9)]
print("ascending:")
for a,b,c in seq:
  print('a={0},b={1},c={2}'.format(a,b,c))
print("descending:")
for a,b,c in seq:
  print('a={2},b={1},c={0}'.format(a,b,c))
