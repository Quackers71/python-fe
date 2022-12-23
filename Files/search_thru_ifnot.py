fhand = open("Files/mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if not "@uct.ac.za" in line:
        continue
    if line.startswith("From:"):
        print(line)
