# Define a function which calculates HCF of two numbers. Define and apply a
# decorator to check whether two given numbers are co-prime or not.


def check_coprime(func):
    def wrapper(num1, num2):
        for i in range(2, min(num1, num2)+1):
            if num1 % i == 0 and num2 % i == 0:
                return "Given numbers are not co-prime"
        return func(num1, num2)
    return wrapper


@ check_coprime
def hcf_two_number(num1, num2):
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1

    for i in range(1, smaller+1):
        if num1 % i == 0 and num2 % i == 0:
            hcf = i

    return hcf


print(hcf_two_number(23, 49))