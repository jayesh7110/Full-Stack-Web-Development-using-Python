# Write a python program to create 2 objects of the user class and assign different
# values.

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def user_details(self):
        print(f"Name is {self.name} and role is {self.role}")


# print the object properties
user1 = User("Mohit", "Accountant")
user2 = User("Dimple", "Executive")
user1.user_details()
user2.user_details()
