# Write a recursive python function to print first N multiples of a given number.

def multiples_number(num, n):
    if n == 0:
        return
    multiples_number(num, n-1)
    print(num * n)


multiples_number(int(input("Enter a number: ")), int(input("Enter a multiples of number: ")))