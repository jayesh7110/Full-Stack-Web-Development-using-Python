# Write a python script to print the octal equivalent of a given decimal number. (do not
# use oct() method)

num = int(input("Enter a decimal number: "))
octal_num = ""

while num > 0:
    octal_num = str(num % 2) + octal_num
    num //= 8

print("The equivalent octal of given number is", octal_num)