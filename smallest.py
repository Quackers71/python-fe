smallest_so_far = 100
print("Staring point",smallest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num < smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far, the_num)

print("Actual smallest No.", smallest_so_far)
