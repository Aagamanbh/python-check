# e=set() # here in sets empty set is defined in this way.
# print(e)
s={1,2,3,4,3,2,90}
a={3,2,5,6,8,76}
print(len(s))
print(s,type(s))
print(s.union(a))
print(s.intersection(a))
s.remove(3)
print(s)
s.clear()
print(s)
a.clear()
print(a)

