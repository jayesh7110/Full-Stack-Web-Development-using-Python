# Write a python program to create a function and print a list where the values are
# square of numbers between 1 and 30.

def square_numbers():
    square_list = []
    for i in range(1, 31):
        square_list.append(i**2)

    return square_list


print(square_numbers())
