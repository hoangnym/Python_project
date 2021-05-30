import pandas as pd
import datetime as dt
import random

# 1. Update the birthdays.csv
birthdays = pd.read_csv("birthdays.csv").to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()

for friend in birthdays:
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    if friend["month"] == now.month and friend["day"] == now.day:
        letter_no = random.choice([1, 2, 3])
        with open(f"letter_templates/letter_{letter_no}.txt") as letter_file:
            content = letter_file.read().replace("[NAME]", friend["name"])
            print(content)
        break



# 4. Send the letter generated in step 3 to that person's email address.




