# Write a Python script to find the smallest number in a given list of numbers.

numbers = [23, 343, 34, 1994, 122, 5, 67, 453, 344, 98]
smaller_num = numbers[0]

for num in numbers:
    if num < smaller_num:
        smaller_num = num

print("Smallest number:", smaller_num)

