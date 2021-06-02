import requests

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall?"
api_key = "fc8716ba7941b8d080f5fc16059dd8c3"

# FFM
MY_LAT = 50.110924
MY_LONG = 8.682127

# Bali
# MY_LAT = -8.340539
# MY_LONG = 115.091949

# NASHVILLE
# MY_LAT = 36.166340
# MY_LONG = -86.779068

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_data = weather_data["hourly"]

# Looping through next 12 hours of hourly data and figure out whether to bring umbrella
twelve_hour_weather_codes = [hour["weather"][0]["id"] for hour in hourly_data][0:12]
will_rain = any(code < 700 for code in twelve_hour_weather_codes)

if will_rain:
    print("Bring an umbrella.")
