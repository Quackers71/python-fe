fruit = "banana"
letter = fruit[1]
print(letter)

x = 3
w = fruit[x - 1]
print(w)

y = len(fruit)
print(y)

index = 0
while index < y:
    letter = fruit[index]
    print(index, letter)
    index += 1

for letter in fruit:
    print(letter)

count = 0
for letter in fruit:
    if letter == "a":
        count += 1
print(count)
