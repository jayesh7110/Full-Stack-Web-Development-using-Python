# Write a python program to create a School class and 3 instance variables and 1 class
# variable.

class School:
    total_school = 0

    def __init__(self, name, location, no_of_students):
        self.name = name
        self.location = location
        self.no_of_students = no_of_students
        School.total_school += 1


s1 = School("ABC School", "New York", 750)
s2 = School("PQR School", "London", 1020)
s3 = School("XYZ School", "New Delhi", 870)

print("Total School created :", School.total_school)
print("School 3 name :", s3.name)
print("School 3 location", s3.location)
print("School 3 no of students :", s3.no_of_students)
