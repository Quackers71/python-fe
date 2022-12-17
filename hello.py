# print("Hello World!")
# x = 2
# print("x =",x)
# x += 2
# print("x + x =",x)

# # Conditional Steps
# y = 5
# print("y =",y)
# if y < 10:
#     print("y < 10")
# if y > 20:
#     print("y !> 20")
# print("Finish")

# # Repeated Steps
# n = 5
# while n > 0 :
#     print(n)
#     n = n - 1  # or use n -= 1
# print("Blastoff!")

# # variables
# hours = 35.0
# rate = 12.50
# pay = hours * rate
# print("pay =",pay)

# # input
# name = input("What's your name? : ")
# print("Hello,",name)

# # input - convert to int
# eurof = input("Europe floor? : ")
# usf = int(eurof) + 1
# print("US floor would be",usf)

# z = 5
# if z > 2:
#     print("Bigger than 2")
#     print("Still Bigger")
# print("Done with", z)

# for i in range(5):
#     # print(i)
#     if i > 2:
#         print("Bigger than", i - 1)
#     print("Done with", i + 1)
# print("All Done")

# x = 25
# if x < 2:
#     print("Small")
# elif x < 10:
#     print("Medium")
# else:
#     print("LARGE")
# print("All Done")

astr = "Hello Bob"
try:
    istr = int(astr)
except:
    istr = -1

print("First", istr)

astr = "123"
try:
    istr = int(astr)
except:
    istr = -1

print("Second", istr)
