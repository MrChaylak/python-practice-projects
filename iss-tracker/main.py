import requests
from datetime import datetime, timezone
import smtplib
import time
import os
from dotenv import load_dotenv

load_dotenv("C:/PyNotes/.env")
MY_EMAIL = os.getenv("MyEmail")
PASSWORD = os.getenv("MyPassword")
EMAIL_PORT = int(os.getenv("EmailPort"))
MY_LAT = float(os.getenv("MyLat"))
MY_LONG = float(os.getenv("MyLon"))


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_latitude, iss_longitude)
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    else:
        return False


def is_night():
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
    time_now = datetime.now(timezone.utc).hour
    print(time_now)
    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False


while True:
    print("check")
    if is_iss_overhead() and is_night():
        print("yes above")
        with smtplib.SMTP("smtp.gmail.com", port=EMAIL_PORT) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Look Up!\n\nThe ISS is above you in the sky."
            )
        time.sleep(60)