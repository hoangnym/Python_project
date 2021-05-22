# Create a new dataframe and save it in csv collecting data: fur color, count

import pandas as pd

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colors = df["Primary Fur Color"]
color_dict = {}

print(color_dict)

for color in colors:
    if color not in color_dict:
        color_dict[color] = 0
    else:
        color_dict[color] += 1

data_dict = {
    "Fur Color": [],
    "Count": [],
}

for key in color_dict:
    data_dict["Fur Color"].append(key)
    data_dict["Count"].append(color_dict[key])

color_df = pd.DataFrame(data_dict)
color_df.to_csv("squirrel_colors.csv")
