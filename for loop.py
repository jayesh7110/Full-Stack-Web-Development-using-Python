# s1 = input("Enter a string :")
# count=0
# for a in s1:
#     if 'a'==a:
#         count += 1
# print("count=",count)

# x = input("Enter a string :")
# for i in x:
#     if i == 'r':
#         break
#     print(i,end='')
# else:
#     print("---All the characters are processed")

# x = "Hello"
# for e in x:
#     print(e,x)

# for i in range(int(input("Enter a number:"))):
#     print((i+1)**2,end=" ")
# print("\n")

# for i in range(int(input("Enter a number:"))):
#     print((i+1)*2,end=" ")
# print("\n")

# for i in range(2*int(input("Enter a number:")),0,-2):
#     # print((i)*2,end=" ")
#     print(i,end=" ")
# print("\n")

# for i in range(int(input("Enter a number:"))):
#     print(((i+1)*2)-1,end=" ")

n = int(input(("Enter a number:")))
sum = 0
for x in range(n+1):
    x = x * x
    sum = x + sum
print(sum)
# for x in range(int(input("Enter a number")))