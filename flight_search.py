import requests
import datetime as dt
from datetime import datetime

TEQUILA_HEADERS = {
    "apikey": "djwzedZxZcznvI2_zoZURgfE-1Ym50wT"
}

TEQUILA_LOCATIONS = "https://api.tequila.kiwi.com/locations/query"
TEQUILA_SEARCH = "https://api.tequila.kiwi.com/v2/search"

DEPARTURE_CITY = "DEL"

class FlightSearch:
    def __init__(self, sheet_data):
        self.sheet_data = sheet_data
        self.city = ""
        self.location_parameters = {
            "term": "",
            "location_types": "city"
        }

        self.search_parameters = {
            "fly_from": DEPARTURE_CITY,
            "fly_to": "",
            "date_from": (datetime.now().date() + dt.timedelta(1)).strftime("%d/%m/%Y"),
            "date_to": (datetime.now().date() + dt.timedelta(6*30)).strftime("%d/%m/%Y"),
            "max_stopovers": 2
        }

    def iata_code_finder(self, city_name):
        self.city = city_name
        self.location_parameters["term"] = self.city
        response = requests.get(TEQUILA_LOCATIONS, params=self.location_parameters, headers=TEQUILA_HEADERS)
        iata_code = response.json()["locations"][0]["code"]
        return iata_code

    def flights_finder(self, iata_code):
        self.search_parameters["fly_to"] = iata_code
        response = requests.get(TEQUILA_SEARCH, params=self.search_parameters, headers=TEQUILA_HEADERS)
        try:
            flight_data = response.json()["data"][0]
            return flight_data
        except IndexError:
            return None

