rawstr = input("Enter a number:")
try:
    ival = float(rawstr)
except:
    ival = -1

if ival > 0:
    print(ival,"is a number")
else:
    print("'",rawstr,"' is not a number")
