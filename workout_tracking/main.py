import requests
import os
import datetime as dt


NUTRI_KEY = os.environ.get('NUTRI_KEY')
NUTRI_APP = os.environ.get('NUTRI_APP')
GENDER = "male"
HEIGHT = "190"
WEIGHT = "85"
NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = 'https://api.sheety.co/acdbb075b8fe1b012668d571d3d22746/myWorkouts/workouts'

headers = {
    'x-app-id': NUTRI_APP,
    'x-app-key': NUTRI_KEY,
    'Content-Type': 'application/json',
}

usr_input = input("What have you done today?")

params = {
    "query": usr_input,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": 33,
}

response = requests.post(NUTRI_ENDPOINT, headers=headers, json=params)
# print(response.text)

data = response.json()

date = dt.datetime.now().strftime("%Y%m%d")
time = dt.datetime.now().strftime("%H%M%S")

headers = {
    'Content-Type': 'application/json',
}

for i in data["exercises"]:
    params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": i['name'],
            "duration": i['duration_min'],
            "calories": i['nf_calories'],
        }
    }

    response = requests.post(SHEETY_ENDPOINT, json=params, headers=headers)
    response.raise_for_status()
    print(response.text)