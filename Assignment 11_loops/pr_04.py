# Write a python script to calculate sum of first N odd natural numbers

n = int(input("Enter a number: "))
sum_odd_natural_num = 0

for i in range(1, n+1):
    odd_number = 2*i - 1
    sum_odd_natural_num += odd_number

print("The sum of the first", n, "odd natural numbers is", sum_odd_natural_num)
