import smtplib

# Account information
my_email = "zenlabdesigninfo@gmail.com"
my_password = "govtK3K5KY&h23ePu^"

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
        msg="Subject:Hello\n\nThis is the body of my email."
    )