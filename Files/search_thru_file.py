fhand = open("Files/mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if line.startswith("From:"):
        print(line)
