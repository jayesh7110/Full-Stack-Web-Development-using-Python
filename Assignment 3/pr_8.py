# Write a python script to store a hexadecimal number 2F in a variable and print it in octal format.

hexadecimal_num = "2F"
integer_num = int(hexadecimal_num, 16)
octal_num = oct(integer_num)
print(octal_num)