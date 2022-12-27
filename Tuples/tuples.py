# using sorted()
d = {'a':10, 'b':1, 'c':22}
t = sorted(d.items())
print("t =",t)

for k, v in t:
    print(k, v)

#  Procedural (Algorithm) - sort by values instead of key
tmp = list()
for k, v,in t:
    tmp.append( (v, k) )
print(tmp)

tmp = sorted(tmp, reverse=True)
print("Reversed :",tmp)

tmp = sorted(tmp, reverse=False)
print("Long version : ",tmp)


# Shorter (Lambda) version of the above - sort by values instead of key
print("Short version :",sorted( [(v,k) for k,v in d.items() ] ) )