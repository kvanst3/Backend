import os
import requests
from twilio.rest import Client
import json


NAME = 'nvidia'
STOCK = "NVDA"
COMPANY_NAME = "NVIDIA Corp."
AA_ENDPOINT = "https://www.alphavantage.co/query"
AA_KEY = os.environ.get('AA_KEY')
NA_ENDPOINT= "https://newsapi.org/v2/everything"
NA_KEY = os.environ.get('NEWSAPI_KEY')
TWILIO_SID = os.environ['TWILIO_SID']
TWILIO_AUTH = os.environ['TWILIO_AUTH']
MY_TEL = os.environ['MY_TEL']


def get_change(current, previous):
    if current == previous:
        return 0
    try:
        return round((current - previous) / previous * 100.0, 2)
    except ZeroDivisionError:
        return 0


params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'outputsize': 'compact',
    'apikey': AA_KEY,
}

response = requests.get(AA_ENDPOINT, params=params)
response.raise_for_status()

data = response.json()

kinou_price = float(data["Time Series (Daily)"][list(data["Time Series (Daily)"].keys())[0]]["4. close"])
ototoi_price = float(data["Time Series (Daily)"][list(data["Time Series (Daily)"].keys())[1]]["4. close"])

# with open("stock_alert/onecall.json", mode="w") as file:
#     json.dump(data, file, indent=4)

percent_change = get_change(ototoi_price, kinou_price)

if abs(percent_change) > 5:
    params = {
        'q': NAME,
        'language': "en",
        'sort_by': "publishedAt",
        'pageSize': '3',
        'apiKey': NA_KEY,
    }

    response = requests.get(NA_ENDPOINT, params=params)
    response.raise_for_status()

    data = response.json()
    up = '🔺'
    down = '🔻'

    for i in range(3):
        client = Client(TWILIO_SID, TWILIO_AUTH)
        message = client.messages \
            .create(
                body=f"{STOCK}: {up if percent_change <0 else down}{abs(percent_change)}%\nHeadlines: {data['articles'][i]['title']}\nBrief: {data['articles'][i]['content']}",
                from_='+17149055219',
                to=MY_TEL
            )

        print(message.status)
