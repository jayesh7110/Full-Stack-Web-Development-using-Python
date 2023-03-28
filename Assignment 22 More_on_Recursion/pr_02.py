# Write a recursive python function to calculate sum of first N odd natural numbers

def sum_odd_natural_numbers(n):
    if n == 1:
        return 1
    return ((n*2)-1) + sum_odd_natural_numbers(n-1)


print(sum_odd_natural_numbers(int(input("Enter a number: "))))