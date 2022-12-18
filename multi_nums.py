def addtwo(a, b):
    added = a + b
    return added

x = input("Enter 1st number: ")
try:
    inp1 = float(x)
except:
    inp1 = -1
    x = 0

if inp1 > 0:
    print("Ok, thanks")
else:
    print("not a number!")

y = input("Enter 2nd number: ")
try:
    inp2 = float(y)
except:
    inp2 = -1
    y = 0

if inp2 > 0:
    print("Ok, thanks")
else:
    print("not a number!")

z = addtwo(int(x), int(y))
if float(z) != 0:
    print("The total is",z)
else:
    print("There was no total...")
