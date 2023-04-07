# Use iter and next method to access all the elements of a given set using while loop

list1 = [1, 2, 3, 4, 5]

it = iter(list1)

while True:
    try:
        element = next(it)
        print(element)
    except StopIteration:
        break

