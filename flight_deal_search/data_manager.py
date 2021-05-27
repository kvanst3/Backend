import os
import json
import requests


class DataManager:

    def __init__(self):
        self.endpoint = "https://api.sheety.co/acdbb075b8fe1b012668d571d3d22746/flightDeals/prices"
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {os.environ.get("D_KEY")}',
        }
        self.iata_code = ''
        self.max_price = ''

    def get_data(self):
        response = requests.get(self.endpoint, headers=self.headers)
        response.raise_for_status()
        print(response.text)
        data = response.json()
        return data

    def edit_data(self, flights_list):
        for flight in flights_list:
            params = {
                "price": {
                    "lowest": flight.price,
                    "link": flight.link,
                    "departure": flight.departure,
                }
            }
            response = requests.put(url=f'{self.endpoint}/{flight.id}', headers=self.headers, json=params)
            response.raise_for_status()
            print(response.text)
