# Write a python script to check if a string contains only numbers.

input_string = "12345"

is_numeric = True

for char in input_string:
    if not char.isdigit():
        is_numeric = False
        break

if is_numeric:
    print("The string content only numeric character")
else:
    print("The string content only non-numeric character")