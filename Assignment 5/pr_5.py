# Write a python script which takes a three digit number from the user and displays
# only its first digit.

num = int(input("Enter a three-digit number: "))

first_digit = num // 100    #new_num = int(str(num)[0])

print("first digit of the given number is",first_digit)