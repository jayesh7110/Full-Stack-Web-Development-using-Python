# Write a Python script to print indices of all occurrences of a given element in a given
# list.

elements = [7, 3, 5, 2, 2, 6, 7, 5, 1, 4, 3, 1]
item = 7
indices = []

for i in range(len(elements)):
    if elements[i] == item:
        indices.append(i)

print(indices)