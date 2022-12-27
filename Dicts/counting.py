counts = dict()
names = ["csev", "cwen", "csev", "zqian", "cwen", "cwen"]
for name in names:
    # if name not in counts:
        counts[name] = counts.get(name, 0) + 1
    # else:
    #     counts[name] += 1
print(counts)

# simplified counting with get()
