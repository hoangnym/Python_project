import pandas as pd
import datetime as dt
import random
import smtplib


def send_mail(sender, sender_pw, recipient, content, subject="Happy Birthday"):
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
    # Update the birthdays.csv
    birthdays = pd.read_csv("birthdays.csv").to_dict(orient="records")

    # Check if today matches a birthday in the birthdays.csv
    now = dt.datetime.now()
    friends = []

    sender_mail = input("What is your email address: ")
    sender_pw = input("What is your email password: ")

    for friend in birthdays:
        if friend["month"] == now.month and friend["day"] == now.day:
            friends.append(friend["name"])
            recipient_mail = friend["email"]
            letter_no = random.choice([1, 2, 3])
            with open(f"letter_templates/letter_{letter_no}.txt") as letter_file:
                letter_content = letter_file.read().replace("[NAME]", friend["name"])
            # 4. Send the letter generated in step 3 to that person's email address.
            send_mail(sender_mail, sender_pw, recipient_mail, letter_content)

    if len(friends) > 0:
        print(f"Emails sent to {friends}")
    else:
        print("No birthdays today.")




