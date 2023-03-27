# Write a python program to multiply all the numbers in a list.

def multiply_number_list(*args):
    print("list of numbers =", list(args))
    mul = 1
    for num in list(args):
        mul *= num

    return mul


m = multiply_number_list(10, 2, 5, 3)
print("multiplication of list of numbers is", m)