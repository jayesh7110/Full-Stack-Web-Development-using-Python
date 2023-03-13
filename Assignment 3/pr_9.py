# Write a python script to store an octal number 125 in a variable and print it in binary format.

octal_num = "125"
integer_num = int(octal_num, 8)
binary_num = bin(integer_num)
print(binary_num)