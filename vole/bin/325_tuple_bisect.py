import bisect

c = [1, 1, 1, 2, 4, 5, 6]
print(bisect.bisect(c, 2))
print(bisect.bisect(c, 4))
print(bisect.insort(c, 3))
print(c)
