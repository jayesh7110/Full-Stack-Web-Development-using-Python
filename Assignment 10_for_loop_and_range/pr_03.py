# Write a python script to print first M multiples of N.

n = int(input("Enter a number: "))
m = int(input("multiples of: "))

for i in range(1, m+1):
    print(i*n)