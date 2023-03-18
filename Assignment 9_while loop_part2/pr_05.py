# Write a python script to print first N odd natural numbers in reverse order

n = int(input("Enter a number: "))
odd_num = 0
i = n*2

while odd_num < n:
    if i % 2 != 0:
        print(i)
        odd_num += 1
    i -= 1
