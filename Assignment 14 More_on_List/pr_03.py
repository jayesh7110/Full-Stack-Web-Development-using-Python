# Write a Python script to create a list of first N even natural numbers.

even_natural_numbers =[]

for n in range(1, int(input("Enter a numbers: "))+1):
    even_natural_numbers.append(2*n)

print("Even Natural Numbers:", even_natural_numbers)