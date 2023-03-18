# Write a menu driven program with the following options:
# a. Check whether a given set of three numbers are lengths of an isosceles triangle or not
# b. Check whether a given set of three numbers are lengths of sides of a right angled triangle or not
# c. Check whether a given set of three numbers are equilateral triangle or not
# d. Exit.

opr = int(input("Menu driven:\n1. three numbers are lengths of an isosceles triangle or not\n2. three numbers are lengths of sides of a right angled triangle or not\n3. three numbers are equilateral triangle or not\n4. Exit\nEnter your choice: "))

match opr:
    case 1:
        x = float(input("Enter a first number: "))
        y = float(input("Enter a second number: "))
        z = float(input("Enter a third number: "))

        if x == y:
            base = z
            height = ((x**2) - ((z/2)**2)) ** 0.5
            area = (base * height) / 2
            print("Area of isosceles: ", area)
        elif x == z:
            base = y
            height = ((x**2) - ((y/2)**2)) ** 0.5
            area = (base * height) / 2
            print("Area of isosceles: ", area)
        elif y == z:
            base = x
            height = ((y**2) - ((x/2)**2)) ** 0.5
            area = (base * height) / 2
            print("Area of isosceles: ", area)
        else:
            print("Not an isosceles triangle")

    case 2:
        x = float(input("Enter a first number: "))
        y = float(input("Enter a second number: "))
        z = float(input("Enter a third number: "))

        if x**2 + y**2 == z**2:
            print("This is a right angle triangle")
        else:
            print("Not an right angle triangle")

    case 3:
        x = float(input("Enter a first number: "))
        y = float(input("Enter a second number: "))
        z = float(input("Enter a third number: "))

        if x == y and y == z:
            print("equilateral triangle")
        else:
            print("Not an equilateral triangle")

    case 4:
        exit()