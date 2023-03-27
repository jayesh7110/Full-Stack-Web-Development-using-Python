# Write a python program to create a function to find the Min of three numbers.

def minimum_number(*num):
    return min(num)


m = minimum_number(14, 26, 13)
print("Minimum number is", m)