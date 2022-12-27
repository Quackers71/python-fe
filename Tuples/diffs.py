l = list()
print("List methods:\n\n",dir(l),"\n")

t = tuple()
print("Tuple methods:\n\n",dir(t),"\n")

# Tuples and Assignment
(x, y) = (4, "Fred")
print("y =",y)

(a, b) = (99, 98)
print("a =",a)

# Tuples and Dictionaries
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k, v) in d.items():
    print("key:",k, "value:",v)

tups = d.items()
print(tups)

# Tuples are Comparable
print((0, 1, 2) < (5, 1, 2))
print((0, 1, 2000000) < (0, 3, 4))
print(('Jones', 'Sally') < ('Jones', 'Sam'))
print(('Jones', 'Sally') > ('Adams', 'Sam'))
