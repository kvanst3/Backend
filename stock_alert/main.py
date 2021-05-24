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


def get_change(current, previous):
    if current == previous:
        return 0
    try:
        return round((abs(current - previous) / previous) * 100.0, 2)
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

# if get_change(kinou_price, ototoi_price) > 5:
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





## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

