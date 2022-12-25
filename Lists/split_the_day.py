fhand = open("Files/mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    words = line.split()
    print(words[2])

email = words[1]
print(email)
pieces = email.split("@")
print(pieces[1])
