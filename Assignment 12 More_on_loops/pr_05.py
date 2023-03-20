# Write a python script to find next prime number of a given number

n = int(input("Enter a starting number to find the next prime number: "))
found = False

while not found:
    n += 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            break
    else:
        found = True

print("The next prime number after", n-1, "is", n)
