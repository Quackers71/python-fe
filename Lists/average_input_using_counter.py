total = 0
count = 0
print("Averge Input using a counter")
print("Enter 'q' to quit.")
while True:
    try:
        inp = input("Enter a number:")
        if inp == "q":
            break
        value = float(inp)
        total += value
        count += 1
    except:
        print("Please enter a correct value or 'q' to quit")

try:
    average = total / count
    print("Average: {:.2f}".format(average))
except:
    print("No value's entered")

# my favourite program up to now with 2 x try/except
