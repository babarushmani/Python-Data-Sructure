# Write a program to find the factors of a no.

# get input from user

num = int(input("type a no to get its factors:"))
result =[]

while num < 2:
    print("no is too small no factors available for 0 and 1")
    break

for i in range(2, num):
        if num % i == 0:
            result.append(i)

else:
 print("given no is prime no factors are available:")

print("The factors are", result)
