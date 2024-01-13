# Python Program to find the L.C.M. of two user input no's

# choose the greater number
x = int(input("Enter 1st no and hit enter"))

y = int(input("Enter 2nd no and hit enter"))

if x > y:
    greater = x
else:
    greater = y

while(True):
       if((greater % x == 0) and (greater % y == 0)):

           lcm = greater
           print(greater)
           break
       greater += 1
       print(greater)



print("The L.C.M. is", lcm)