fhand = open("Files/mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
    # if line.find('From:') >= 0:
        print(line)
