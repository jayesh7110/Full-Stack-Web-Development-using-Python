# Write a python script to print all Prime numbers between two given numbers (both
# values inclusive)

start = int(input("Enter a starting number for prime: "))
end = int(input("Enter a ending number for prime: "))

for num in range(start, end+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break

        else:
            print(num, end=" ")
print()