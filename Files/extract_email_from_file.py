fhand = open("Files/mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if "media" in line:
        sppos0 = line.find(" ")
        atpos = line.find("@")
        sppos1 = line.find(" ",atpos)
        addr = line[sppos0+1 : sppos1]
        if line.startswith("From: "):
            print(addr)
