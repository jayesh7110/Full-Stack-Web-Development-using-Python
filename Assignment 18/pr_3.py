# Create dictionary
country_dict = {"India":"New Delhi","USA":"Washington D.C","Canada":"Ottawa","United Kingdom":"London","China":"Beijing","France":"Paris"}

# Create blank list for retrive data
value_list = []
# Get the value using loop with value() method
for value in country_dict.values():
    # Append the value in list
    value_list.append(value)

# Print list
print(value_list)