# Write a recursive python function to print cubes of first N natural numbers

def cube_natural_numbers(n):
    if n == 0:
        return
    cube_natural_numbers(n-1)
    print(n**3)


cube_natural_numbers(int(input("Enter a number: ")))