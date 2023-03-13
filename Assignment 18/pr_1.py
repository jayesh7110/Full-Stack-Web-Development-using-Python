# Create blank dictionary
my_dict = {}

# Getting input name from user 
name = input("Enter a name: ")
# Getting input age from user
age = int(input("Enter a age: "))
if age < 0:
    age =input(input("Enter valid age!!!  age:"))
gender = input("Enter a gender: ")

#Update dictionary
my_dict['name'] = name
my_dict['age'] = age
my_dict['gender'] = gender

# Print dictionary``
print(my_dict)




