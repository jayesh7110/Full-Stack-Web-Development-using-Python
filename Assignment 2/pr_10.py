# Write a python script to display the current date and time. First create variables to
# store date and time, then display date and time in proper format (like: 13-8-2022 and
# 9:00 PM)

import datetime

current_date_time = datetime.datetime.now()


current_date = datetime.datetime.now().strftime("%d-%m-%Y")
current_time = datetime.datetime.now().strftime("%I:%m %p")
print(current_date, current_time)
