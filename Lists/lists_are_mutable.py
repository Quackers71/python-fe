fruit = "Banana"
try:
    fruit[0] = "b"
except:
    fruit = fruit
    print("Exception - This string is immutable!")

x = fruit.lower()
print(fruit,"converted using .lower() is",x)

lotto = [2, 14, 26, 41, 63]
print(lotto)

pos = 2
newnum = 28
print("changing position", pos, "to", newnum)
lotto[pos] = newnum
print(lotto)
