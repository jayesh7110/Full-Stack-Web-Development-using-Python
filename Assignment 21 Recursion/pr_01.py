# Write a recursive python function to print first N natural numbers.

def natural_numbers(n):
    if n > 0:
        natural_numbers(n-1)
        print(n)


natural_numbers(int(input("Enter a number: ")))