# Write a recursive python function to print a number in reverse order.

def reverse_order_number(n):
    if n < 10:
        print(n)
    else:
        print(n % 10, end="")
        reverse_order_number(n // 10)


reverse_order_number(int(input("Enter a number: ")))