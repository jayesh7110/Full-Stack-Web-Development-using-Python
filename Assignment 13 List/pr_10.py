# Write a Python script to create a list, where each element of the list is a digit of a
# given number.

number = input("Enter a number: ")
digits = []

for n in number:
    digits.append(int(n))

print("digits:", digits)