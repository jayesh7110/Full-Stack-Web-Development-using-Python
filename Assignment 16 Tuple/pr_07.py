# Write a python program to copy elements 4 and 5 from the following tuple into a new
# tuple. tuple1=(1,2,3,4,5,6)

tuple1 = (1, 2, 3, 4, 5, 6)

tuple_one = list(tuple1)
list_two = []

for i in tuple_one:
    if i == 4:
        list_two.append(i)
    else:
        if i == 5:
            list_two.append(i)

final_tuple = tuple(list_two)
print(final_tuple)

# two_tuple = tuple1[3:5]
# print(two_tuple)