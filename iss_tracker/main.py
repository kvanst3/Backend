import requests
from datetime import datetime


# response = requests.get("http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# iss_data = response.json()

params = {
    "lat": 50.915726,
    "lng": 4.259706,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=params)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]['sunset'].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)
