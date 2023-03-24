# Write a python script to check if a string contains only characters of the alphabet.

input_string = "King"
is_string = True

for char in input_string:
    if not char.isalpha():
        is_string = False
        break

if is_string:
    print("The string content only alphabet character")
else:
    print("The string content only non-alphabet character")