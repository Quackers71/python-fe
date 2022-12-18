from colorama import Fore, Style

def addtwo(a, b):
    added = a + b
    return added

def trycatch(n):
    try:
        inp = float(n)
    except:
        inp = -1

    if inp > 0:
        print("Ok, thanks")
    else:
        print(Fore.RED + "not a number!" + Style.RESET_ALL)

v = input("Enter 1st number: ")
trycatch(v)

w = input("Enter 2nd number: ")
trycatch(w)

x = input("Enter 3rd number: ")
trycatch(x)

y = input("Enter 4th number: ")
trycatch(y)

if v.isnumeric() and w.isnumeric() and x.isnumeric() and y.isnumeric():
    z = addtwo(int(x), int(y))
    print("The total is",z)
else:
    print("There was no total...")
