# Write a python script to print all Prime numbers under 100

n = 100
for num in range(1, n+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=",")

print()