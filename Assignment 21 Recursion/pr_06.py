# Write a recursive python function to print first N even natural numbers in reverse
# order.

def even_reverse_numbers(n):
    if n == 0:
        return
    print(n*2)
    even_reverse_numbers(n-1)


even_reverse_numbers(int(input("Enter a number: ")))

