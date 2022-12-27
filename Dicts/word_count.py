counts = dict()
line = input("Enter a line of text: ")
words = line.split()

print("Words:",words)
print("Counting...")

for word in words:
    counts[word] = counts.get(word, 0) + 1
print("Counts",counts)

# definite loop in Dict
for key in counts:
    print(key, counts[key])

# using the list() method
print(list(counts))
print(list(counts.keys()))
print(list(counts.values()))
print(list(counts.items()))

for wrd,cnt in counts.items():
    print(wrd, cnt)

# the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car
