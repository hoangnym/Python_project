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
# print(type(data))                       # dataframe
# print(type(data["temp"]))               # series

data_dict = data.to_dict()
# print(data_dict)

# Calculate average temperature
temp_list = data["temp"].to_list()
avg_temp = sum(temp_list) / len(temp_list)
print(avg_temp)
print(data["temp"].mean())
print(data["temp"].max())

# Get first row
row_1 = data[data.day == "Monday"]
# print(row_1)

# Get row of maximum temp day
row_2 = data[data.temp == data.temp.max()]
# print(row_2)

# Get temperature of monday in fahrenheit
monday_temp = int(data[data.day == "Monday"].temp) * (9/5) + 32
# print(monday_temp)


# Create dataframe from scratch
data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 65, 65]
}

df = pd.DataFrame(data_dict)
df.to_csv("new_data.csv")
print(df)