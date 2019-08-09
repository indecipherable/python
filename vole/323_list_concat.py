x = [4, None, 'foo']
# extending is less expensive than concatenating
x.extend([5,6,(7,8)])
print(x)
print(x[5])
