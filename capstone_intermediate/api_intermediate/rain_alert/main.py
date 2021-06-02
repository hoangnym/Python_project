# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import requests

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall?"
api_key = ""

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = ""
auth_token = ""

# FFM
MY_LAT = 50.110924
MY_LONG = 8.682127

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
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It is going to rain today. Remember to bring an ☔️.",
        from_="", # your twilio number
        to="" # your verified number
    )

    print(message.status)
