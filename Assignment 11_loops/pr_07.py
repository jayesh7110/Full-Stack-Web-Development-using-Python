# Write a python script to count digits in a given number

num = int(input("Enter a number: "))
count = 0

while num != 0:
    count += 1
    num //= 10

print("The number of digits in the given number is:", count)

