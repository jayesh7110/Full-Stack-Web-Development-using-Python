# Write a python script to check whether a given pair of numbers are co-Prime
# numbers or not.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

min_num = min(a, b)
for i in range(2, min_num+1):
    if a % i == 0 and b % i == 0:
        print("%d and %d are not co-prime" % (a, b))
        break
else:
    print("%d and %d are co-prime" % (a, b))
