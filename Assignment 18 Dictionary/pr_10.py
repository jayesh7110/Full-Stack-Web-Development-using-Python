# Write a python program to get the key of lowest value from the dictionary.
# sample_dict = {
# 'C': 92,
# 'Java': 66,
# 'Python': 85
# }


sample_dict = {
    'C': 92,
    'Java': 66,
    'Python': 85
}

# find the minimum value using 'min' function for the value
minimum_value = min(sample_dict.values())

# iterate the loop though find key
for key, value in sample_dict.items():
    if value == minimum_value:
        print("The lowest value for key is", key)
