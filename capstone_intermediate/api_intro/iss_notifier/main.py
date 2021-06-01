import requests
from datetime import date, datetime
import smtplib

MY_LAT = 50.110924
MY_LONG = 8.682127


def can_see_iss(my_lat=MY_LAT, my_long=MY_LONG):
    my_lat_min = my_lat - 5
    my_lat_max = my_lat + 5
    my_long_min = my_long - 5
    my_long_max = my_long + 5
    if my_lat_min <= iss_latitude <= my_lat_max and my_long_min <= iss_longitude <= my_long_max:
        return True
    else:
        return False


def send_mail(sender, sender_pw, recipient, content, subject="Spot ISS now."):
    try:
        # Establish and close connection
        with smtplib.SMTP("smtp.gmail.com") as connection:
            # Secure connection
            connection.starttls()
            # Login by providing account information
            connection.login(user=sender, password=sender_pw)
            # Send Mail
            connection.sendmail(
                from_addr=sender,
                to_addrs=recipient,
                msg=f"Subject:{subject}\n\n{content}"
            )
            print("Email successfully sent.")
    except ConnectionError:
        print("Could not establish connection")


if __name__ == '__main__':
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

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

    time_now = datetime.now()
    now_hour = time_now.hour

    #If the ISS is close to my current position and it is currently dark
    if not can_see_iss() and not (sunrise > now_hour or sunset < now_hour):
        # Then send me an email to tell me to look up.
        mail = "zenlabdesigninfo@gmail.com"

        content_mail = "Look up into the sky. You can see the ISS now from your position."
        send_mail(mail, mail_pw, mail_pw, content_mail)

    # BONUS: run the code every 60 seconds.



