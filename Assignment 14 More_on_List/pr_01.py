# Write a Python script to create a list of first N natural numbers.

natural_numbers = []

for n in range(1, int(input("Enter a number: "))+1):
    natural_numbers.append(n)

print("Natural_numbers:", natural_numbers)