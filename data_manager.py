import requests
from flight_search import FlightSearch

SHEETY_ENDPOINT = " YOUR SHEETY.CO ENDPOINT"
SHEETY_CONFIG = {
    "price": {
        "iataCode": ""
    }
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, sheet_data):
        self.sheet_data = sheet_data

    def update_destination_codes(self):
        flight_search = FlightSearch(self.sheet_data)
        for city in self.sheet_data["prices"]:
            city_name = city["city"]
            id = city["id"]
            iata_code = flight_search.iata_code_finder(city_name)
            SHEETY_CONFIG["price"]["iataCode"] = iata_code
            requests.put(f"{SHEETY_ENDPOINT}/{id}", json=SHEETY_CONFIG)

