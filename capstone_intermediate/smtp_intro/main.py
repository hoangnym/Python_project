import smtplib
import datetime as dt
import random

# Account information
my_email = "zenlabdesigninfo@gmail.com"
my_password = "govtK3K5KY&h23ePu^"

def send_mail(subject, content):
    try:
        # Establish and close connection
        with smtplib.SMTP("smtp.gmail.com") as connection:
            # Secure connection
            connection.starttls()
            # Login by providing account information
            connection.login(user=my_email, password=my_password)
            # Send Mail
            connection.sendmail(
                from_addr=my_email,
                to_addrs="minhhoangn0608@gmail.com",
                msg=f"Subject:{subject}\n\n{content}"
            )
            print("Email successfully sent.")
    except:
        print("Could not establish connection")

# Get current weekday date and time
now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 6:
    with open("quotes.txt", "r") as quotes_file:
        quotes = quotes_file.read().splitlines()

    random_quote = random.choice(quotes)

    send_mail("Your Motivational Sunday Boost", random_quote)



