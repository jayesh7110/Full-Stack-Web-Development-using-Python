# Write a Python script to create a list of first N odd natural numbers.

odd_natural_numbers = []

for n in range(1, int(input("Enter a number:"))+1):
    odd_natural_numbers.append(n*2-1)

print("Odd Natural Numbers:", odd_natural_numbers)