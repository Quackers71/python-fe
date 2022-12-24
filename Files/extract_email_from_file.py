fhand = open("Files/mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if "edu" in line:
        sppos0 = line.find(" ")
        atpos = line.find("@")
        if line.startswith("From: "):
            print(line[6:])
