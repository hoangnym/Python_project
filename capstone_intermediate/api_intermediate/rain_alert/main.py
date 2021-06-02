import requests

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall?"
api_key = "fc8716ba7941b8d080f5fc16059dd8c3"
MY_LAT = 50.110924
MY_LONG = 8.682127

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

print(hourly_data)