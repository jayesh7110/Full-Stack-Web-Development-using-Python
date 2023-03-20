# Write a python script to calculate sum of squares of first N natural numbers

n = int(input("Enter a number: "))
sum_square_num = 0

for i in range(1, n+1):
    sum_square_num += i**2

print("The sum of the first", n, "square numbers is", sum_square_num)