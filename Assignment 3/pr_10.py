# Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal) and display the result in binary format.

octal_num = "25"
hexadecimal_num = "39"
oct_to_int = int(octal_num, 8)
hexa_to_int = int(hexadecimal_num, 16)

int_sum = oct_to_int + hexa_to_int
print(bin(int_sum))