# Write a python script to check whether two given strings are identical, first string comes before the
# second in dictionary order or first string comes after the second string in dictionary order using match case statement

str1 = input("Enter a first string: ")
str2 = input("Enter a second string: ")

match (str1, str2):
    case (str1, str2) if str1 == str2:
        print("Strings are identical")
    case (str1, str2) if str1 < str2:
        print("first string comes before te second in dictionary order")
    case (st1, str2) if str1 > str2:
        print("first string comes after the second string in dictionary order")