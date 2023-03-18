# Write a program which takes user’s age and display the category of person. Age below 10 years- Kid,
# Age below 20 - Teen, Age below 40 - young, Age below 60 - Experienced, Age above or equal 60 - Senior Citizen.

age = int(input("Enter your age: "))

match age:

    case age if age < 10:
        category = "Kid"
    case age if age < 20:
        category = "Teen"
    case age if age < 40:
        category = "Young"
    case age if age < 60:
        category = "Experience"
    case age if age >= 60:
        category = "Senior Citizen"

if age >= 0:
    print("Your age is", age, "and category is", category)
else:
    print("Invalid age!!!")