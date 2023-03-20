# Write a python script to calculate sum of cubes of first N natural numbers

n = int(input("Enter a number: "))
sum_cube_num = 0

for i in range(1, n+1):
    sum_cube_num += i**3

print("The sum of the first", n, "cube numbers is", sum_cube_num)