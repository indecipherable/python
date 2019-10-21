a_list = [ 2, 5, 9, None ]
tup = ('foo', 'bar', 'baz')
b_list = list(tup)
b_list[1] = 'eekbarbadurkle'
b_list.append('morty')
b_list.insert(1,'brad')
b_list.pop()
print(b_list)
b_list.pop(0)
print(b_list)
