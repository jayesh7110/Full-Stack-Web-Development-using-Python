# Write a python script to remove the last digit from a given number. (for example, if
# user enters 2534 then your output should be 253)

num = int(input("Enter a number:"))

last_digit = num // 10     #new_num =  int(str(num)[:-1])
print("The number without last digit",last_digit)