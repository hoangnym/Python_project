weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# To convert temp_c into temp_f: (temp_c * 9/5) + 32 = temp_f
def temp_f(temp_c):
    return (temp_c * 9/5) + 32

weather_f = {day:temp_f(temp_c) for (day, temp_c) in weather_c.items()}

# Write your code 👇 below:

print(weather_f)


