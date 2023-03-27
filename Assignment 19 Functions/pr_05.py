# Write a python program to create a function which expects a list as an argument.

def list_args(*args):
    print("List of arguments =", list(args))


list_args(1, 2, 3, 4)