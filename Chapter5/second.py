#  sets

#  empty set

e = set()
print(type(e))

s = {3,45,87,2,3,7,4,6}
print(s)
print(type(s))

#  methods

print(len(s))

#  remove method

s.remove(3)
print(s)

s1 = {3,54,6,3,7,1}
s2 = {1,3,7,4,9,10}

print(s1.union(s2))
print(s1.intersection(s2))