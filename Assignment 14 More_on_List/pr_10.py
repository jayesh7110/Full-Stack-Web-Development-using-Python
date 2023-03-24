# Write a python script to sort a list.

elements = [7, 3, 5, 2, 2, 6, 7, 5, 1, 4, 3, 1]

n = len(elements)
# Traverse through all array elements
for i in range(n):
    # Last i elements are already sorted
    for j in range(0, n - i - 1):
        # Swap if the element found is greater than the next element
        if elements[j] > elements[j + 1]:
            elements[j], elements[j + 1] = elements[j + 1], elements[j]

print(elements)