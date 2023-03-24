# 8. Write a python program to convert two lists into a dictionary in a way that item from
# list1 is the key and item from list2 is the value.

list1 = ['a', 'b', 'c', 'd', 'e']
list2 = [1, 2, 3, 4, 5]


two_list_dictionary = {list1[i]: list2[i] for i in range(len(list1))}

print(two_list_dictionary)


mylist = {}
for i in range(len(list1)):
    mylist[list1[i]] = list2[i]

print(mylist)