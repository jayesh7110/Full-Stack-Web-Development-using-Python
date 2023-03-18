# Write a python program to check whether a given number is positive, negative or zero using match case statement

num = int(input("Enter a number: "))

match num:
    case num if num > 0:
        print(num, "is positive")
    case num if num < 0:
        print(num, "is negative")
    case 0:
        print(num, "is zero")
