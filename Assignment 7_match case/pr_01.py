# Write a python script to display the number of days in a given month number.

month = int(input("Enter a month number (1-12): "))

match month:
    case 2:
        print("28 or 29 days")
    case 4, 6, 9, 11:
        print("30 days")
    case _:
        print("31 days")
