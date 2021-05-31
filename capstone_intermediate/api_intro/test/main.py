import requests
from datetime import datetime

MY_LAT = 50.110924
MY_LONG = 8.682127

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # 1xx Hold on, 2xx here you go, 3xx go away, 4xx you screwed up, 5xx I screwed up
# response.raise_for_status()
#
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(sunrise)
print(sunset)


time_now = datetime.now()
print(time_now.hour)