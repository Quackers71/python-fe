print(range(4))

friends = ["Joe", "Gary", "Sally"]
print(len(friends))

print(range(len(friends)))

for friend in friends:
    print("Merry Xmas:", friend)

print(friend[0])
print(friends[0])

for i in range(len(friends)):
    friend = friends[i]
    print("Merry Xmas: ", friend, len(friend), range(len(friend)))
