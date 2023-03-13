# Write a python script which takes a three digit number from the user and displays
# only its middle digit.

number = int(input("Enter a three-digit number: "))

middle_digit = (number % 100) // 10           # middle_digit = int(str(number)[1])

print("The middle digit of the number is:", middle_digit)
