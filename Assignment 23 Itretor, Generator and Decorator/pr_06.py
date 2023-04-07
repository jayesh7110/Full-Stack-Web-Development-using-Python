# Create a generator to produce first n prime numbers

def produce_prime(n):
    for num in range(2, n+1):
        is_prime = True
        for i in range(2, int(num ** 0.5)+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num

for e in produce_prime(int(input("Enter a number: "))):
    print(e)