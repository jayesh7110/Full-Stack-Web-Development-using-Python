# Write a python script to calculate sum of first N natural numbers

n = int(input("Enter a number: "))
sum_natural_num = 0

for i in range(1, n+1):
    sum_natural_num += i

print("The sum of the first", n, "natural numbers is", sum_natural_num)