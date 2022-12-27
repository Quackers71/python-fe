
import os
dir = 'Dicts/'
files = os.listdir(dir)
txt_files = [f for f in files if f.endswith('.txt')]
# print(txt_files)
print("\nList of files in the ",dir," directory with a .txt extension.\n",sep="")
for f in txt_files:
    print(f)

print("\nEnter the filename with or without the .txt extension")

try:
    name = input("Enter file: ")
    
    if len(name) < 1:
            filename = dir + "clown.txt"
    else:
        filename = dir + name + ".txt"

    if filename.endswith('.txt.txt'):
        # print(filename,"0")
        base = os.path.basename(filename)
        # print("base:",base)
        split_text = os.path.splitext(base)
        # print("split_text:",split_text)
        split_final = os.path.splitext(base)[0]
        # print("split_final:",split_final)
        filename = dir + split_final
        # print(filename,"1")
    
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

    bigcount = None
    bigword = None
    for word,count, in counts.items():
        if bigcount is None or count > bigcount:
            bigword = word
            bigcount = count

    print("This word '",bigword,"' appeared ",bigcount," times",sep="")
except:
    print("\nThe file doesn't exist")
