# Write a recursive python function to calculate sum of the digits of a given number

def sum_digit_of_number(n):
    if n < 10:
        return n
    return n % 10 + sum_digit_of_number(n // 10)


print(sum_digit_of_number(int(input("Enter a number: "))))