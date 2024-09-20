import pandas
import random
import smtplib
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv("C:/PyNotes/.env")
MY_EMAIL = os.getenv("MyEmail")
PASSWORD = os.getenv("MyPassword")
EMAIL_PORT = int(os.getenv("EmailPort"))

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
birthday_dict_list = data.to_dict(orient="records")
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day

for birthday in birthday_dict_list:
    if birthday["month"] == month and birthday["day"] == day:
        age = now.year - birthday["year"]
        print(age)
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name
# from birthdays.csv
        rand_letter_index = random.randint(1, 3)
        with open(f"./letter_templates/letter_{rand_letter_index}.txt") as letter:
            contents = letter.read()
            new_letter = contents.replace("[NAME]", birthday["name"])
            print(new_letter)
# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", port=EMAIL_PORT) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday["email"],
                msg=f"Subject:Happy {age}th Birthday!\n\n{new_letter}"
            )



