#Write a python script to get the last digit from a given number. (for example, if user
# enters 2089 then your output should be 9)

num = int(input("Enter a number:"))

last_digit = num % 10     #new_num = int(str(num)[-1])
print("last digit is",last_digit)