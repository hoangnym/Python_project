# print each line of weather data
# with open("weather_data.csv") as weather_data:
#     data = weather_data.read().splitlines()
#     print(data)


import csv

with open("weather_data.csv") as weather_data:
    data = csv.reader(weather_data)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
    print(temperatures)