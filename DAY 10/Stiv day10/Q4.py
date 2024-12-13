import random
set1={random.randint(1,50) for _ in range(10)}
print(set1)
set2={72,66,55}
print(set2)
a=set1.union(set2)
print(a)
a.remove(55)
print(a)
a.update({10,20,30})
print(a)
a.pop()
print(a)
a.clear()
print(a)