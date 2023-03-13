# 10. Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.

num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))
num3 = int(input("Enter a third number: "))

if num1 > num2 and num1 > num3:
    print("first number is maximum",num1)
elif num2 > num3 and num2 > num1:
    print("second number is maximum",num2)
else:
    print("third number is maximum",num3)