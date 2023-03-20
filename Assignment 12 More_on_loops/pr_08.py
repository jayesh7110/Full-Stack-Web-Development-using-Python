# Write a python script to print first N terms of a Fibonacci series

n = int(input("Enter a number:"))
a = 0
b = 1
sum_num = 0

print("Fibonacci sequence:")
for i in range(1, n+1):
    if n <= 0:
        print("Please enter a positive number")

    elif n == 1:
        print(a)
    else:
        print(sum_num, end=" ")
        a = b
        b = sum_num
        sum_num = a + b
print()