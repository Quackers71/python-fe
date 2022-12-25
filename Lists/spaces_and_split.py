line = "A lot           of  spaces"
etc = line.split()
print("line = ",'"',line,'"',sep="")
print("etc =",etc)

line = "first;second;third"
thing = line.split()
print("line =",'"',line,'"',sep="")
print("thing =",thing)
print("elements of thing =",len(thing))

thing = line.split(";")
print("thing now =",thing)
print("elements of thing =",len(thing))
