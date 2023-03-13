def sum(n):
    if n == 1:
        return 1
    return n*n + sum(n-1)

s = sum(int(input("Enter a number: ")))
print("Sum of square :",s)
