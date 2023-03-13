# Write a python script to calculate simple interest

P = int(input("Enter a principal: "))
R = float(input("Enter a rate of interest: "))
N = int(input("Enter a time: "))

I = (P*R*N)/100

print("Interest is",I)