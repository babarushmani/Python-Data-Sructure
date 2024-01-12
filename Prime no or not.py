# Write a program to check whether a number is prime or not.

# get input from user

num = int(input("type any no and hit enter:"))

if num >=2:
    for i in range(2, num):
        print("All no's tried is", i)
        if num%i == 0:
            print("\nfalse,", "divisor is",  i)
            break
    else:
     print("\ntrue, Given value", num, "is a prime no.")

else:
    print("false, you have entered" , num, "which is not a prime no.")