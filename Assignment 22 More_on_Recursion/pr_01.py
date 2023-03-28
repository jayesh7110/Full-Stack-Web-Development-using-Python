# Write a recursive python function to calculate sum of first N natural numbers

def sum_natural_numbers(n):
    if n == 1:
        return 1
    return n + sum_natural_numbers(n-1)


print(sum_natural_numbers(int(input("Enter a number: "))))