# Write a Python script to remove all non int values from a list.

element_list = ["my", 232, 56, "hello", 786, "code", 343.34]
new_list = []

for element in element_list:
    if type(element) == int:
        new_list.append(element)

print("Updated int list:", new_list)
