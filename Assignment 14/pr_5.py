l1 = list(input("Enter a number used by seprated comma(,): ").split(","))
l1 = [int(x) for x in l1]
print("Smallest number:",min(l1))