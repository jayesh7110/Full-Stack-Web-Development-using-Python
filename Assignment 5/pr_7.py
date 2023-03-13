# Write a python script which takes a three digit number from the user and displays
# only its last digit.

number = int(input("Enter a three-digit number: "))

last_digit = number % 10

print("The last digit of the number is",last_digit)