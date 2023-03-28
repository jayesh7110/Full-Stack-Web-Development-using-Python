# Write a recursive python function to print first N odd natural numbers

def odd_natural_numbers(n):
    if n == 0:
        return
    odd_natural_numbers(n-1)
    print((n * 2) - 1)


odd_natural_numbers(int(input("Enter a number: ")))