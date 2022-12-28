import re

# Original string parsing
data = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
atpos = data.find("@")
# print(atpos)
sppos = data.find(" ",atpos)
# print(sppos)
host = data[atpos+1 : sppos]
print(host)

# Double Split Pattern
words = data.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])

# Regex
extract = re.findall('^From .*@([^ ]*)',data)
# extract = re.findall('@([^ ]*)',data)
print(extract)

# for i in extract:
#     j = i
# print(j)
