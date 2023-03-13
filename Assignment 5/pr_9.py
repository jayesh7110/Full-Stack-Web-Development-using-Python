# Write a python script to use NOT IN operator to display the data not present in list

list1 = [ int(x) for x in input("Enter a number with separated by space: ").split()]

element = int(input("Enter a element to search for: "))

if element not in list1:
    print(element,"is not presented in the list")
else:
    print(element,"is presented in the list")