import requests
import numpy
import smtplib
from datetime import datetime
from user_info import my_email, my_password, destination_email

MY_LAT = 50.915726
MY_LNG = 4.259706


def is_dark():
    params = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]['sunset'].split("T")[1].split(":")[0])

    time_now = datetime.now()

    return True if time_now.hour > sunset or time_now.hour < sunrise else False


def iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_data = response.json()
    iss_lat = float(iss_data["iss_position"]["latitude"])
    iss_lng = float(iss_data["iss_position"]["longitude"])

    return True if MY_LNG in numpy.arange(iss_lng - 5, iss_lng + 5) and MY_LAT in numpy.arange(iss_lat - 5, iss_lat + 5) else False


if is_dark() and iss_overhead():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=destination_email,
            msg=f"Subject:ISS Tracker!\n\nLook up!"
        )
