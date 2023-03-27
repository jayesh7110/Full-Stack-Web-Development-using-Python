# Write a python program to create a function that accepts a string and calculate the
# number of upper case letters and lower case letters.

def string_calculator(str_check):
    lower_latter = 0
    upper_latter = 0
    print("string =", str_check)
    for s in str_check:
        if s.islower():
            lower_latter += 1
        elif s.isupper():
            upper_latter += 1

    print("lower latter is", lower_latter)
    print("upper latter is", upper_latter)


string_calculator("Python Programming Language")