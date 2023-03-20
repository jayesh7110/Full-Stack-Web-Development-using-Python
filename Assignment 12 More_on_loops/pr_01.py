# Write a python script to reverse a number.

num = int(input("Enter a number: "))
reverse_num = 0

while num > 0:
    digit = num % 10
    reverse_num = (reverse_num*10) + digit
    num //= 10

print("The reverse number of given number is",reverse_num)