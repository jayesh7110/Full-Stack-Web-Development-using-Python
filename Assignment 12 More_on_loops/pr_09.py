# Write a python script to calculate LCM of two numbers

num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))

if num1 > num2:
    max_num = num1
else:
    max_num = num2

while True:
    if max_num % num1 == 0 and max_num % num2 == 0:
        lcm = max_num
        break
    max_num += 1

print("LCM of", num1, "and", num2, "is", lcm)