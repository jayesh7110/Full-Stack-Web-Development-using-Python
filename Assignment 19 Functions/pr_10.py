# Write a python program to create a function to check whether a given number is even
# or odd.

def odd_even(num):
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")


odd_even(int(input("Enter a number: ")))