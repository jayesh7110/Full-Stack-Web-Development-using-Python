# Create a generator to produce first n terms of Fibonacci series

def fibonacci_produce(n):
    a = 0
    b = 1
    for num in range(1, n+1):
        yield a
        a, b = b, a+b


for e in fibonacci_produce(int(input("Enter a number: "))):
    print(e)