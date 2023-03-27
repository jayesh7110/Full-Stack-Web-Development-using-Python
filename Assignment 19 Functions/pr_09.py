# Write a python program to create a function to check whether a number falls in a
# given range.

def number_in_range(num, low, high):
    if num in range(low, high+1):
        return True
    else:
        return False

print("Number falls in range:", number_in_range(23, 10, 20))
