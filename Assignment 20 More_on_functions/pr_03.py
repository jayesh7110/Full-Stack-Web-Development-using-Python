# Write a python program to create a function that prints the even numbers from a
# given list.
# Sample List :
def even_numbers(num):

    for n in num:
        if n % 2 == 0:
            print(n)


even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])