# Write a python script to calculate sum of digits of a given number

num = int(input("Enter a number: "))
sum_num = 0

while num != 0:
    digit = num // 10
    sum_num = sum_num + num % 10
    num = digit

print("Sum of digits:", sum_num)