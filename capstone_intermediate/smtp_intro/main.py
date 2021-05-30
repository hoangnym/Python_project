import smtplib
import datetime as dt
import random


def send_mail(sender_mail, sender_pw, subject, content):
    try:
        # Establish and close connection
        with smtplib.SMTP("smtp.gmail.com") as connection:
            # Secure connection
            connection.starttls()
            # Login by providing account information
            connection.login(user=sender_mail, password=sender_pw)
            # Send Mail
            connection.sendmail(
                from_addr=sender_mail,
                to_addrs="minhhoangn0608@gmail.com",
                msg=f"Subject:{subject}\n\n{content}"
            )
            print("Email successfully sent.")
    except ConnectionError:
        print("Could not establish connection")


# Get current weekday date and time
now = dt.datetime.now()
day_of_week = now.weekday()
sender = input("Your email: ")
sender_password = input("Your email password: ")

if day_of_week == 6:
    with open("quotes.txt", "r") as quotes_file:
        quotes = quotes_file.read().splitlines()

    random_quote = random.choice(quotes)

    send_mail(sender, sender_password, "Your Motivational Sunday Boost", random_quote)



