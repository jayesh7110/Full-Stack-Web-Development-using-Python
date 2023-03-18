# Write a python program to check whether a given string is a multiword string or single word string using
# match case statement


string_words = input("Enter a string: ")

match string_words:
    case  string_words if " " in string_words:
        print("multiword string")

    case string_words:
        print("single word string")




