abc = "With three words"
stuff = abc.split()
print("abc = ", '"',abc,'"',sep="")
print("elements in abc =",len(abc))
print("abc string split() =",stuff)
print("list count =",len(stuff))
print("position [0] =",stuff[0])

i = 0
for w in stuff:
    i += 1
    print(i-1, w)
