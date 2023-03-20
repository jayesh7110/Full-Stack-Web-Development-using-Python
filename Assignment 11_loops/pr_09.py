# Write a python script to print binary equivalent of a given decimal number. (do not
# use bin() method)

num = int(input("Enter a decimal number: "))
binary_num = ""

while num > 0:
    binary_num = str(num % 2) + binary_num
    num //= 2

print("The binary equivalent of the given number for", binary_num)