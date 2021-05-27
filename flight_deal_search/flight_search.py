import requests
import json
import datetime as dt
import os
from dateutil.relativedelta import relativedelta


class FlightSearch:

    def __init__(self, fly_to, price, row_id):
        self.endpoint = "https://tequila-api.kiwi.com/v2/search"
        self.headers = {
            'apikey': os.environ.get('KIWI_KEY')
        }
        self.id = row_id
        today = dt.datetime.now()
        later = today + relativedelta(months=+6)
        self.params = {
            "fly_from": "BRU",
            "fly_to": fly_to,
            "dateFrom": today.strftime('%d/%m/%Y'),
            "dateTo": later.strftime('%d/%m/%Y'),
            "price_to": price,
            "max_stopovers": "1",
            "sort": "price",
            "limit": "5"
        }
        self.price = 0
        self.departure = ""
        self.link = ""

        self.search_flight()

    def search_flight(self):
        response = requests.get(self.endpoint, headers=self.headers, params=self.params)
        response.raise_for_status()
        self.get_cheapest(response)
    
    def get_cheapest(self, response):
        data = response.json()
        if len(data['data']) > 0:
            self.price = data['data'][0]['price']
            self.link = data['data'][0]['deep_link']
            self.departure = data['data'][0]['local_departure']
