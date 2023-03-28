# Write a recursive python function to print first N odd natural numbers in reverse order

def odd_reverse_numbers(n):
    if n == 0:
        return
    print((n*2)-1)
    odd_reverse_numbers(n-1)


odd_reverse_numbers(int(input("Enter a number: ")))