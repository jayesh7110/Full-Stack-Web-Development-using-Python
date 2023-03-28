# Write a recursive python function to print octal of a given decimal number

def decimal_to_octal(n):
    if n == 0:
        return ''
    else:
        return decimal_to_octal(n // 8) + str(n % 8)


print(decimal_to_octal(64))