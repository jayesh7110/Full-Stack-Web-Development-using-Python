# Write a python script to check whether a given number is a three-digit number or not.

number = int(input("Enter a number:"))

if len(str(number)) == 3:
    print(number,"is a three-digit number")
else:
    print(number,"is a not three-digit number")