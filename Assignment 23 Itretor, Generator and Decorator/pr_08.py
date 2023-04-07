# Create an endless iterator using generator method to produce Prime numbers

def produce_endless_prime():
    num = 2
    while True:
        is_prime = True
        for i in range(2, int(num ** 0.5)+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1

it = produce_endless_prime()
prime_series = []
while True:
    ans = input("Do you want generate prime element [y/n] ? ").lower()
    if ans == 'y':
        x = next(it)
        prime_series.append(x)
    else:
        break

print(prime_series)