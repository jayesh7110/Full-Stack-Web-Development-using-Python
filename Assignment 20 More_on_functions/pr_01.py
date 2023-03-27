# Write a python program to create a function that takes a list and returns a new list
# with the original list's unique elements.

def list_with_unique_numbers(num):
    unique_nums = []
    for n in num:
        if n not in unique_nums:
            unique_nums.append(n)

    return unique_nums


numbers = [10, 3, 6, 8, 4, 3, 5, 6]
print("unique numbers =", list_with_unique_numbers(numbers))