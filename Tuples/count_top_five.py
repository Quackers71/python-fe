import os
dir = 'Dicts/'
files = os.listdir(dir)
txt_files = [f for f in files if f.endswith('.txt')]
# print(txt_files)
print("\nList of files in the ",dir," directory with a .txt extension.\n",sep="")
for f in txt_files:
    print(f)

try:
    name = input("Enter file: ")
        
    if len(name) < 1:
        filename = dir + "clown.txt"
    else: 
        filename = dir + name + ".txt"

    fhand = open(filename,'r')
    contents = fhand.read()
    print("Contents:\n",contents,"\n",sep="")
    fhand.close()

    fhand = open(filename)

    counts = dict()
    for line in fhand:
        words = line.split()
        for word in words:
            # idiom: retrieve/create/update counter
            counts[word] = counts.get(word, 0) + 1

    # print("Counts:",counts)

    tmp = list()
    for k,v in counts.items():
        # print(k,v)
        newt = (v,k)
        tmp.append(newt)

    # print("Flipped :",tmp)

    tmp = sorted(tmp, reverse=True)
    # print("Sorted :",tmp[:5])

    print("\nThe top 5 words and counts\n")

    for v,k in tmp[:5]:
        print(k,v)

except:
    print("\nThe file doesn't exist")
