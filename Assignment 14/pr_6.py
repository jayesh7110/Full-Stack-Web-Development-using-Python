l1 = list(input("Enter a number used seprated by comma(,): ").split(","))
l1 = [int(x) for x in l1]
print("Sum of elements:",sum(l1))