han = open("Files/mbox-short.txt")
for line in han:
    line = line.rstrip()
    # print("line:",line)
    wds = line.split()
    # print("wds:",wds)
    # *** guardian ***
    # if len(wds) < 3:
    #     continue
    # *** guardian - in a compound statement ***
    if len(wds) < 3 or wds[0] != "From":
        continue
    print("Day of the week:",wds[2])