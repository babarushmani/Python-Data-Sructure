# Python Program to find the L.C.M. of two input number

x = int(input("Enter 1st no and hit enter"))
y = int(input("Enter 2nd no and hit enter"))


# choose the greater number
if x > y:
  greater = x
else:
  greater = y

z = x * y

for i in range(2 , z):
    if((greater % x == 0) and (greater % y == 0)):
        lcm = greater
        break

    greater += 1





print("The L.C.M. is", lcm)