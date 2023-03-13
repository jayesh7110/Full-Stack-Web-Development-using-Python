# Write a python script to check whether a given quadratic equation has two real &
# distinct roots, real & equal roots or imaginary roots

a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + (discriminant)**0.5) / (2*a)
    root2 = (-b - (discriminant)**0.5) / (2*a)
    print("The quadratic equation has two real and distinct roots:", root1, "and", root2)
elif discriminant == 0:
    root = -b / (2*a)
    print("The quadratic equation has real and equal roots:", root)
else:
    real_part = -b / (2*a)
    imag_part = (-discriminant)**0.5 / (2*a)
    print("The quadratic equation has imaginary roots:", real_part, "+", imag_part, "i and", real_part, "-", imag_part, "i")
