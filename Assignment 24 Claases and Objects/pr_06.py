# Write a python program to create 3 user objects and find the youngest of all.

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


u1 = User("Ankit", 23)
u2 = User("Sagar", 19)
u3 = User("Rashmi", 27)

youngest = u1

if u2.age < youngest.age:
    youngest = u2
if u3.age < youngest.age:
    youngest = u3

print(f"{youngest.name} is the youngest with age {youngest.age}")
