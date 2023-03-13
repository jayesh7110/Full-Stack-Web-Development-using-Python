sortList = list(input("Enter a number used by seprate by space: ").split(" "))
sortList = [int(i) for i in sortList]
sortList.sort()
print(sortList)