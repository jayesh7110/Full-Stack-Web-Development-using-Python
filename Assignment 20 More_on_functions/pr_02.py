# Write a python program to create a function that takes a number as a parameter and
# checks if the number is prime or not.

def prime_number(num):
    if num < 2:
        print("Not Prime")
        return
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")


prime_number(22)
prime_number(7)
