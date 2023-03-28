# Write a recursive python function to calculate sum of first N even natural numbers

def sum_even_natural_numbers(n):
    if n == 1:
        return 2
    return (n*2) + sum_even_natural_numbers(n-1)


print(sum_even_natural_numbers(int(input("Enter a number: "))))