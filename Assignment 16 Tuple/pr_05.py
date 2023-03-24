# Write a python program to check if all items in the tuple are the same.

t1 = (5, 5, 6, 5)

all_same = True
for i in range(len(t1)):
    if t1[i] != t1[0]:
        all_same = False
        break

if all_same:
    print("All element in tuple are the same")
else:
    print("All element in tuple are the not same")