# Write a recursive python function to calculate sum of squares of first N natural
# numbers

def sum_square_natural_numbers(n):
    if n == 1:
        return 1
    return n**2 + sum_square_natural_numbers(n-1)


print(sum_square_natural_numbers(int(input("Enter a number: "))))