# Write a python script to check whether a given number is Prime or not

num = int(input("Enter a number: "))

if num < 2:
    print("Not a Prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a Prime")
            break
    else:
        print("Prime number", num)