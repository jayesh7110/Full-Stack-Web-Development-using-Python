# Write a python script to print first 10 odd natural numbers in reverse order

num_odd = 0
i = 19

while num_odd < 10:
    if i % 2 != 0:
        print(i)
        num_odd += 1
    i -= 1