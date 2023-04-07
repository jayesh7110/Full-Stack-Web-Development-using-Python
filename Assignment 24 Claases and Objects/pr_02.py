# Write a python program to create a user class with a method to greet the user.

class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}")


user1 = User("Jenish")
user1.greet()