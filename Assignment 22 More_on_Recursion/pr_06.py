# Write a recursive python function to calculate the factorial of a number.

def factorial_number(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_number(n-1)


print(factorial_number(int(input("Enter a number: "))))