# Write a python program to add items from another set to the current set. thisset =
# {"Java", "Python", "SQL"}
# secondset= {"C", "Cpp", "NoSQL"}

this_set = {"Java", "Python", "SQL"}

second_set= {"C", "Cpp", "NoSQL"}

for element in second_set:
    this_set.add(element)

print(this_set)