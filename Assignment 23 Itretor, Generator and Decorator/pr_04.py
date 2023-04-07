# Create a generator to produce squares of first N natural numbers

# def square_produce(n):
#     a = 1
#     while n:
#         yield a ** 2
#         a += 1
#         n -= 1
#
#
# for e in square_produce(int(input("Enter a number:"))):
#     print(e)


def square_produce(nums):
    for num in range(1, nums+1):
        yield num ** 2


for square_num in square_produce(int(input("Enter a number: "))):
    print(square_num)
