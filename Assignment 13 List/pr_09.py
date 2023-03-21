# Write a Python script to create a list of city names taken from the user.

city_names = []

for i in range(1, int(input("Enter how many city name you want: "))+1):
    city = input("Enter city name: ")
    city_names.append(city)

print("City names:", city_names)