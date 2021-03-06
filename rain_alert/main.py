import requests
from twilio.rest import Client
import json
import os

MY_LAT = os.environ.get("MY_LAT")
MY_LNG= os.environ.get("MY_LNG")
MY_KEY = os.environ.get("OWM_KEY")
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

account_sid = os.environ['TWILIO_SID']
auth_token = os.environ['TWILIO_AUTH']

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": MY_KEY,
    "exclude": "current,daily,minutely",
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

data = response.json()

# with open("rain_alert/onecall.json", mode="w") as file:
#     json.dump(data, file, indent=4)

hrly_data = data["hourly"][:12]
will_rain = False
for i in hrly_data:
    if i['weather'][0]['id'] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="Gon'rain",
            from_='+17149055219',
            to=os.environ['MY_TEL']
        )

    print(message.status)
