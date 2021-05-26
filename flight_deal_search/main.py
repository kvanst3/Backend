from flight_search import FlightSearch
from data_manager import DataManager


data_manager = DataManager()
destinations = data_manager.get_data()

for destination in destinations:
    
# fligh = (FlightSearch("YTO", "450"))