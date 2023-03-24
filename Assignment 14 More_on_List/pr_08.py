# Write a Python script to print distinct elements along with their frequencies of
# occurrence in the list.

elements = [7, 3, 5, 2, 2, 6, 7, 5, 1, 4, 3, 1]
distinct_element = []

for element in elements:
    found = False
    for item in distinct_element:
        if element == item[0]:
            item[1] += 1
            found = True
            break

    if not found:
        distinct_element.append([element, 1])

for element in distinct_element:
    print(element[0], "appears", element[1], "times")