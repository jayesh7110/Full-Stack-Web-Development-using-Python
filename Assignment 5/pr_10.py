# Write a python script to use IS operator to display if both variables are the same
# object or not?

# var1 = input("Enter the first variable: ")
# var2 = input("Enter the second variable: ")
#
# if var1 is var2:
#     print("Both variables are the same object.")
# else:
#     print("Both variables are different objects.")

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)
print(x is z)