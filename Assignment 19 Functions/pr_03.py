# Write a python program to create a function which expects an unknown number of
# arguments.

def unknown_number_argument(*args):
    print("The number of argument is:", len(args))
    for arg in args:
        print(arg)


unknown_number_argument(1, 2, 3, 4)