# Write a recursive python function to print first N natural numbers in reverse order

def reverse_natural_numbers(n):
    if n > 0:
        print(n)
        reverse_natural_numbers(n-1)


reverse_natural_numbers(int(input("Enter a number: ")))