# Write a python script to print first N natural numbers in reverse order

n = int(input("Enter a number:"))
i = 1

while i <= n:
    print(n-i+1)
    i += 1