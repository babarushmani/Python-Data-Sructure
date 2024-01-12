# Write a program to find the factors of a no.

# get input from user

num = int(input("type a no to get its factors:"))

result =()

if num< 2:
    print("no is too small no factors available for 0 and 1")

for i in range(2, num+1):
          if num%i == 0:
              print(i)
else:
    print("no factors available given no is prime.")