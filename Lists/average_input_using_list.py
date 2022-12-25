numlist = list()
print("Averge Input using a List")
print("Enter 'q' to quit.")
while True:
    try:
        inp = input("Enter a number:")
        if inp == "q":
            break
        value = float(inp)
        numlist.append(value) # append method
    except:
        print("Please enter a correct value or 'q' to quit")

try:
    average = sum(numlist) / len(numlist)
    print("Average: {:.2f}".format(average))
except:
    print("No value's entered")
