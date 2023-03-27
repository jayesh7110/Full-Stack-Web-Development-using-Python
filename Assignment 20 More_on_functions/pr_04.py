# Write a python program to create a function that checks whether a passed string is
# palindrome or not.

def palindrome_string(str1):
    return "Palindrome string" if str1 == str1[::-1] else "Not Palindrome string"


p = palindrome_string("level")
print(p)