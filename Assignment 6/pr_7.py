# Write a python script to check whether a given number is positive, negative or zero.

number = float(input("Enter a number:"))

if number == 0:
    print(number,"is zero")
elif number > 0:
    print(number, "is a positive")
else:
    print(number,"is a negative")