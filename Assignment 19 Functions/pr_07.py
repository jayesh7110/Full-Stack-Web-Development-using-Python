# Write a python program to sum all the numbers in a list.

def sum_number_list(*args):
    print("list of numbers =", list(args))
    return sum(list(args))


sum_list = sum_number_list(12, 34, 23, 16)
print("sum of all the numbers in list is", sum_list)