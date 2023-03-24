# Write a python program to Sort a tuple of tuples by the second item.
# tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))

tuple1 = (('a', 21), ('b', 37), ('c', 11), ('d', 29))

n = len(tuple1)
for i in range(n):
    for j in range(n-i-1):
        if tuple1[j][1] > tuple1[j+1][1]:
            # create a new tuple with the elements in the desired order
            temp = (tuple1[j+1][0], tuple1[j+1][1])
            tuple1[j+1] = (tuple1[j][0], tuple1[j][1])
            tuple1[j] = temp

print(tuple1)
