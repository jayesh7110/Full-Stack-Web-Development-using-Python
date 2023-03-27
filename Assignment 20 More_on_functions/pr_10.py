# Write a python program to create a function to check whether a string is an anagram
# or not.

def is_anagram(str1, str2):

    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False

    return sorted(str1) == sorted(str2)


a = is_anagram("anagram", "nag a ram")      #("abc", "def")

if a:
    print("string is anagram")
else:
    print("string is not anagram")