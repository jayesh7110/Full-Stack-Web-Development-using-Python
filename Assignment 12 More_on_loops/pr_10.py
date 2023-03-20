# Write a python script to calculate HCF of two numbers

num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))

if num1 > num2:
    smaller = num2
else:
    smaller = num1
for i in range(1, smaller+1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i

print("HCF of", num1, "and", num2, "is", hcf)
