# print each line of weather data
# with open("weather_data.csv") as weather_data:
#     data = weather_data.read().splitlines()
#     print(data)

# import csv

# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd

data = pd.read_csv("weather_data.csv")
print(type(data))                       # dataframe
print(type(data["temp"]))               # series

data_dict = data.to_dict()
print(data_dict)

# Calculate average temperature
temp_list = data["temp"].to_list()
avg_temp = sum(temp_list) / len(temp_list)
print(avg_temp)