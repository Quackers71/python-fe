import re
x = "We just received $10.00 for cookies"
y = re.findall('\$[0-9.]+',x)
for i in y:
    y = i
print("The cookies cost :",i)
