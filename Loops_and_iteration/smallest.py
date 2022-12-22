smallest = None
print("Staring point",smallest)
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)

print("Actual smallest No.", smallest)
