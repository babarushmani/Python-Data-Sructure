# Python Program to find the L.C.M. of two input number

def compute_lcm(x, y):

   # choose the greater number
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

   return lcm

num1 = int(input("Enter 1st no and hit enter"))
num2 = int(input("Enter 2nd no and hit enter"))

print("The L.C.M. is", compute_lcm(num1, num2))