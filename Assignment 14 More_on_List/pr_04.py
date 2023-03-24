# Write a Python script to find the greatest number in a given list of numbers.

numbers = [23, 343, 34, 1994, 122, 67, 453, 344, 98]
max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num

print("Greatest number:", max_num)