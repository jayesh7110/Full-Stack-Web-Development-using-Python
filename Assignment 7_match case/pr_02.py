# Write a menu driven program to perform following operations - Addition, Subtraction, Multiplication, Division

num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))

opr = int(input("operations :-\n1 for Addition(+)\n2 for Subtraction(-)\n3 for Multiplication(*)\n4 for Division(/)\nEnter your choice: "))
match opr:
    case 1:
        print("Addition is", num1+num2)
    case 2:
        print("Subtraction is", num1-num2)
    case 3:
        print("Multiplication is", num1*num2)
    case 4:
        print("Division is", num1/num2)

