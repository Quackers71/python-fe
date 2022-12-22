# from colorama import Fore, Style

def addfour(a, b, c, d):
    added = a + b + c + d
    
    return added

def trycatch(n):
    try:
        inp = float(n)
    except:
        inp = -1

    if inp > 0:
        print("Ok, thanks")
    else:
        print("not a number!")
        # print(Fore.RED + "not a number!" + Style.RESET_ALL)

v = input("Enter 1st number: ")
trycatch(v)

w = input("Enter 2nd number: ")
trycatch(w)

x = input("Enter 3rd number: ")
trycatch(x)

y = input("Enter 4th number: ")
trycatch(y)

if v.isnumeric() and w.isnumeric() and x.isnumeric() and y.isnumeric():
    z = addfour(int(v), int(w), int(x), int(y))
    print("The total is",z)
else:
    print("There was no total...")
