# Write a recursive python function to calculate sum of cubes of first N natural numbers

def sum_cube_natural_numbers(n):
    if n == 1:
        return 1
    return n**3 + sum_cube_natural_numbers(n-1)


print(sum_cube_natural_numbers(int(input("Enter a number: "))))