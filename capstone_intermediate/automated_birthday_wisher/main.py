import smtplib

# Account information
my_email = "zenlabdesigninfo@gmail.com"
my_password = "govtK3K5KY&h23ePu^"

# Establish connection
connection = smtplib.SMTP("smtp.gmail.com")

# Secure connection
connection.starttls()

# Login by providing account information
connection.login(user=my_email, password=my_password)

# Send Mail
connection.sendmail(from_addr=my_email, to_addrs="minhhoangn0608@gmail.com", msg="Hello")

# Close connection
connection.close()