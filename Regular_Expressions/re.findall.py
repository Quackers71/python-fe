import re
x = "My 2 favourite numbers are 7, 14, 15, 19 and 42"
y = re.findall('[0-9]+',x)
print("Extracted: ",y)

# Greedy vs Non-Greedy matching
a = "From: Using the : character"
b = re.findall('^F.+?:',a)
# b = re.findall('^F.+:',a) # Greedy
print(b)

c = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
d = re.findall('^From (\S+@\S+)',c)
# d = re.findall('\S+@\S+',c)
print(d)

# ChatGPT 
# nums = re.findall(r'\b\d+\b', x)
# print("Extracted: ",nums)
