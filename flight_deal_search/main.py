from flight_search import FlightSearch
from data_manager import DataManager


data_manager = DataManager()
destinations = data_manager.get_data()

flights = []
for destination in destinations['prices']:
    flight = FlightSearch(destination['iataCode'], destination['maxPrice'], destination['id'])
    flights.append(flight)

data_manager.edit_data(flights)
