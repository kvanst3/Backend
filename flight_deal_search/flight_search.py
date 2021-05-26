import requests
import json
import datetime as dt
import os


class FlightSearch:

    def __init__(self, fly_to, price):
        self.endpoint = "https://tequila-api.kiwi.com/v2/search"
        self.headers = {
            'apikey': os.environ.get('KIWI_KEY')
        }

        self.params = {
            "fly_from": "BRU",
            "fly_to": fly_to,
            "dateFrom": "1/06/2021",
            "dateTo": "1/10/2021",
            "price_to": price,
            "max_stopovers": "1",
            "sort": "price",
            "limit": "5"
        }

        self.search_flight()
        self.price = 0
        self.airline = ""
        self.departure

    def search_flight(self):
        response = requests.get(self.endpoint, headers=self.headers, params=self.params)
        response.raise_for_status()
        get_cheapest(response)
    
    def get_cheapest(response):
        data = response.json()
        self.price = data['data'][0]['price']
        self.airline = data['data'][0]['airlines'][0]
        self.departure = data['data'][0]['local_departure']