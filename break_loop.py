while True:
    line = input("> ")
    if line == 'done':
        break
    elif line == '':
        continue
    else:
        print(line)
print("We're all finished here!")
