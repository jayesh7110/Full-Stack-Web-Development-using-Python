# Write a python script to print first 10 even natural numbers in reverse order

num_even = 0
i = 20

while num_even < 10:
    if i % 2 == 0:
        print(i)
        num_even += 1
    i -= 1