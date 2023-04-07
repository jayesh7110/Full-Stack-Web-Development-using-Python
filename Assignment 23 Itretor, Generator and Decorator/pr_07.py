# Create an endless iterator using generator method to produce terms of Fibonacci
# series

def produce_endless_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


it = produce_endless_fibonacci()
fibo_series = []
while True:
    ans = input("Do you want to generate element [y/n] ? :").lower()
    if ans == 'y':
        x = next(it)
        fibo_series.append(x)
    else:
        break

print(fibo_series)