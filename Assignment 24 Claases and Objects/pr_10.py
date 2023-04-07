# Define a class Employee with instance object variables empid, name, salary. Write
# __init__() method in the class to initialize instance object variables. Also define
# instance methods to input fields and display field values

class Employee:
    def __init__(self, empid, name, salary):
        self.empid = empid
        self.name = name
        self.salary = salary

    def input_field(self):
        self.empid = input("Enter a employee id :")
        self.name = input("Enter a name :")
        self.salary = int(input("Enter a salary :"))

    def display_field(self):
        print(f"Employee id is {self.empid}")
        print(f"Employee name is {self.name}")
        print(f"Employee salary is {self.salary}")


e1 = Employee("E01", "Sidhu", 25000)
e1.display_field()

e1.input_field()
e1.display_field()