# Write a python program to create three dictionaries, then create one dictionary that
# will contain the other three dictionaries.

num1 = {1, 3, 4}
num2 = {2, 5, 7}
num3 = {6, 7}

alpha_digit = {1: {'a': 1}, 2: {'b': 2}, 3: {'c': 3}}

combined_dict = {"num1": num1, "num2": num2, "num3": num3, "alpha_digit": alpha_digit}
print(combined_dict)

