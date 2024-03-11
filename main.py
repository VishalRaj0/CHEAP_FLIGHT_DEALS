import requests
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

sheety_endpoint = "YOUR SHEETY.CO ENDPOINT"
response_get = requests.get(sheety_endpoint)
sheet_data = response_get.json()

data_manager = DataManager(sheet_data)
flight_search = FlightSearch(sheet_data)
notification_manager = NotificationManager()

for arrival_city in sheet_data["prices"]:
    flight_details = flight_search.flights_finder(arrival_city["iataCode"])
    if flight_details is None:
        notification_manager.flight_not_found_notification()
        continue

    price = flight_details["price"]
    if price <= arrival_city["lowestPrice"]:
        departure_date = flight_details["local_departure"].split("T")[0]
        city_from = flight_details["cityFrom"]
        city_code_from = flight_details["cityCodeFrom"]
        notification_manager.send_notification(price=price, to=arrival_city, city_from=city_from,
                                               city_code_from=city_code_from, date=departure_date)
