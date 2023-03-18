# Write a program to display day name on the basis of user’s liking of a colour. Ask user for his favorite colour.
# User can answer in a sentence like “I like red colour”. Assuming all colour name entered by user is in lowercase.
# Use match case to display day name associated with the colour.
# a. Yellow - Monday
# b. Blue - Tuesday
# c. Orange - Wednesday
# d. White - Thursday
# e. Black - Friday
# f. Red - Saturday
# g. All other colours - Sunday

fav_colour = input("Enter your favorite colour: ").lower()

match fav_colour:
    case c if "yellow" in c:
        print("Monday")
    case c if "blue" in c:
        print("Tuesday")
    case c if "orange" in c:
        print("Wednesday")
    case c if "white" in c:
        print("Thursday")
    case c if "black" in c:
        print("Friday")
    case c if "red" in c:
        print("Saturday")
    case _:
        print("Sunday")