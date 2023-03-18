# Write a python script to print first N even natural numbers

n = int(input("Enter a number: "))
even_num = 0
i = 2

while even_num < n:
    if i % 2 == 0:
        print(i)
        even_num += 1
    i += 1
