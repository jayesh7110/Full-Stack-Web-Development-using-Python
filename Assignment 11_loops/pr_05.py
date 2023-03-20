# Write a python script to calculate sum of first N even natural numbers

n = int(input("Enter a number: "))
sum_even_natural_num = 0

for i in range(1, n+1):
    even_num = i*2
    sum_even_natural_num += even_num

print("The sum of the first", n, "even natural numbers is", sum_even_natural_num)