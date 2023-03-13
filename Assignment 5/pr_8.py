# Write a python script to use IN operator to display the data present in the list

list1 = [ int(x) for x in input("Enter a number with separated by space: ").split()]
element = int(input("Enter a element search for: "))

if element in list1:
    print(element,"is presented in the list")
else:
    print(element,"is not presented in the list")