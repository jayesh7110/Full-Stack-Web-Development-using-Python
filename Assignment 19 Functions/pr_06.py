# Write a python program to create a function that finds a maximum of four numbers.

def maximum_four(a, b, c, d):
    if a >= b and a >= c and a >= d:
        return a
    elif b >= a and b >= c and b >= d:
        return b
    elif c >= a and c >= b and c >= d:
        return c
    else:
        return d


m = maximum_four(14, 20, 15, 8)
print("maximum of four numbers is", m)