print("Hello World!")
x = 2
print("x =",x)
x += 2
print("x + x =",x)

# Conditional Steps
y = 5
print("y =",y)
if y < 10:
    print("y < 10")
if y > 20:
    print("y !> 20")
print("Finish")

# Repeated Steps
n = 5
while n > 0 :
    print(n)
    n = n - 1  # or use n -= 1
print("Blastoff!")

# variables
hours = 35.0
rate = 12.50
pay = hours * rate
print("pay =",pay)

# input
name = input("What's your name? : ")
print("Hello,",name)

# input - convert to int
eurof = input("Europe floor? : ")
usf = int(eurof) + 1
print("US floor would be",usf)
