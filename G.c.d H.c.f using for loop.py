# Python Program to find the L.C.M. of two input number

x = int(input("Enter 1st no and hit enter"))
y = int(input("Enter 2nd no and hit enter"))

# choose the greater number
if x > y:
  smaller = y
else:
  smaller = x

z = x * y

for i in range(2 , smaller-1):
    if ((x % i == 0) and (y % i == 0)):
        gcd = i
        print(i)

print("The G.C.d or H.c.f is", gcd)