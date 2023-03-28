# Write a recursive python function to find the Nth term of the Fibonacci series.

def fibonacci_series(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fibonacci_series(n-1) + fibonacci_series(n-2)


print(fibonacci_series(int(input("Enter a number: "))))