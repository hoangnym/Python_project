import pandas as pd
import datetime as dt

# 1. Update the birthdays.csv
birthdays = pd.read_csv("birthdays.csv").to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
day = now.day
month = now.month

for friend in birthdays:



# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




