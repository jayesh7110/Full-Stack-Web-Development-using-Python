# Write a python script to print greater between two numbers. Print number only once
# even if the numbers are the same.

num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))

if num1 > num2:
    print(num1,"is greater")
elif num1 < num2:
    print(num2,"is greater")
else:
    print("Both are equal")


