# Write a python program to append elements from another list to the current list.(
# firstlist = ["Java", "Python", "SQL"]
# secondlist = ["C", "Cpp", "NoSQL"] )

firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]

print("firstlist:", firstlist, "\nsecondlist:", secondlist)

for item in secondlist:
    firstlist.append(item)

print("\nUpdated firstlist:", firstlist)
