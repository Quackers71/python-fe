import re

fhand = open("Files/mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if re.search('^X-\S+:',line):
    # if re.search('^X.*:',line):
    # if re.search('^From:',line):
        print(line)
