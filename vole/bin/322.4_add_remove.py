a_list = [ 2, 5, 9, None ]
tup = ('foo', 'bar', 'baz')
b_list = list(tup)
b_list[1] = 'eekbarbadurkle'
b_list.append('morty')
b_list.insert(1,'brad')
print("'morty' in b_list:")
print('morty' in b_list)
print("'morty' not in b_list:")
print('morty' not in b_list)
