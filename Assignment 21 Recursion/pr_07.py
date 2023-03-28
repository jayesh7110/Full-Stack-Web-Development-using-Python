# Write a recursive python function to print squares of first N natural numbers

def square_numbers(n):
    if n == 0:
        return
    square_numbers(n-1)
    print(n**2)


square_numbers(int(input("Enter a number: ")))