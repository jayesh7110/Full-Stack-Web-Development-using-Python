# Write a python program to delete the age property of the user.

class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email


u1 = User("Raj", 35, "raj01@gmail.com")
del u1.age
print(u1.__dict__)
