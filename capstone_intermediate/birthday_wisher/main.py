import pandas as pd
import datetime as dt
import random
import smtplib


def send_mail(recipient, content,
              subject="Happy Birthday", my_email="zenlabdesigninfo@gmail.com", my_password="govtK3K5KY&h23ePu^"):
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

    for friend in birthdays:
        if friend["month"] == now.month and friend["day"] == now.day:
            recipient_mail = friend["email"]
            letter_no = random.choice([1, 2, 3])
            with open(f"letter_templates/letter_{letter_no}.txt") as letter_file:
                letter_content = letter_file.read().replace("[NAME]", friend["name"])
            # 4. Send the letter generated in step 3 to that person's email address.
            send_mail(recipient_mail, letter_content)






