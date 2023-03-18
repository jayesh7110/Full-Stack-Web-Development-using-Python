# Write a python script to print first N odd natural numbers

n = int(input("Enter a number: "))
odd_num = 0
i = 1

while odd_num < n:
    if i % 2 != 0:
        print(i)
        odd_num += 1
    i += 1