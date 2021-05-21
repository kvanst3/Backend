import requests
import numpy
from datetime import datetime
from user_info import my_email, my_password. destination_email

MY_LAT = 50.915726
MY_LNG = 4.259706

def lat_in_range(my_lat, iss_lat):
    return True if my_lat in numpy.arange(iss_lat - 5, iss_lat + 5) else False

def lng_in_range(my_lng, iss_lng):
    return True if my_lng in numpy.arange(iss_lng - 5, iss_lng + 5) else False

def is_dark(time_now, sunrise, sunset):
    return True if time_now.hour > sunset or time_now.hour < sunrise else False

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()
iss_data = response.json()
iss_lat = float(iss_data["iss_position"]["latitude"])
iss_lng = float(iss_data["iss_position"]["longitude"])

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

if is_dark(time_now, sunrise, sunset) and lat_in_range(MY_LAT, iss_lat) and lng_in_range(MY_LNG, iss_lng):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=destination_email,
            msg=f"Subject:ISS Tracker!\n\nLook up!"
        )
