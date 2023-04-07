# Write a python program to create a user class with 3 properties : name, age, email.

class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email


# Create a new user object with specific properties
my_user = User("Sachin", 28, "sachin@hotmail.com")

# print out the user's properties
print("Name:", my_user.name)
print("Age:", my_user.age)
print("Email:",my_user.email)