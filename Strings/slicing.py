s = "Monty Python"
print(s[0:4])

# Remember, upto but not including...
print(s[6:7])

print(s[6:20])
print(len(s))

print(s[:2])
print(s[8:])
print(s[:])

# String concatenation
a = "Hello"
b = a + "There"
print(b)

c = a + " " + "There"
print(c)

# Logical Operator
fruit = "banana"
print("fruit =", fruit)
print("'n' in fruit:","n" in fruit)
print("'m' in fruit:","m" in fruit)
print("'nan' in fruit:","nan" in fruit)

if "a" in fruit:
    print("Found an 'a'")

# String comparison
if fruit == "banana":
    print("All right,",fruit,"s.",sep="")


word = "orange"
if word < fruit:
    print("Your word," + word + ", comes before", fruit)
elif word > fruit:
    print("Your word," + word + ", comes after", fruit)
else:
    print("All right,",word,"s.",sep="")

# String library methods
greet = "Hello Bob"
zap = greet.lower()
print(zap)
print(greet)
print("Hi There".lower())

stuff = "Hello World"
print(type(stuff))
print(dir(stuff))

# Searching a string
pos = fruit.find("na")
print("pos =",pos)

bb = "b"
aa = fruit.find(bb)
if aa == -1:
    print("There is no",bb ,"in your string")
else:
    print("The letter",bb ,"is in position",aa)

#Search and replace
nstr = greet.replace("Bob", "Jane")
print(nstr)

nstr2 = greet.replace("o", "X")
print(nstr2)

#Stripping whitespace
greeting = "    Hello Bobby     "
print(greeting.lstrip())
print(greeting.rstrip())
print(greeting.strip())

#Prefixes
line = "Please have a nice day"
print(line.startswith("Please"))
print(line.startswith("p"))

# Parsing and Extracting
data = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:17 2009"
print("The data is ","'",data,"'",sep="")

atpos = data.find("@")
print("@ is at pos",atpos)

# find the next space after the @ position
sppos = data.find(" ",atpos)
print("The next space after the @ is at pos",sppos)

host = data[atpos+1 : sppos]
print("Extracted address is ","'",host,"'",sep="")

# In Python 3, all strings are Unicode
