# Write a python program to init default values for user object using __init__ method.

class User:
    def __init__(self, name="Guest", role="User"):
        self.name = name
        self.role = role

    def get_details(self):
        print(f"user name is {self.name} and role is {self.role}")


# get the object properties
user1 = User()
user2 = User("Admin", "Admin")

# print the object properties values
user1.get_details()
user2.get_details()