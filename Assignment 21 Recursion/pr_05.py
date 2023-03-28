# Write a recursive python function to print first N even natural numbers.

def even_natural_numbers(n):
    if n == 0:
        return
    even_natural_numbers(n-1)
    print(n*2)


even_natural_numbers(int(input("Enter a number: ")))