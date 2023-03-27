# Write a python program to access a function inside a function.

def add(a, b):
    return a + b


def main():
    a = add(3, 5)
    print("print sum of two numbers is", a)


main()