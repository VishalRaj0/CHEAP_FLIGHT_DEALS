from twilio.rest import Client

ACCOUNT_SID = "ACa24898c0f17645d4382da0666b4354e7"
AUTH_TOKEN = "33eb031b88da60aa5cb28ecfc236f76b"

CLIENT = Client(ACCOUNT_SID, AUTH_TOKEN)
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_notification(self, **kwargs):
        message = CLIENT.messages.create(
            from_="+19049005420",
            to="+917769932142",
            body=f"Price: EUR {kwargs['price']} \n"
                 f"Departure from: {kwargs['city_from']} ({kwargs['city_code_from']}) \n"
                 f"Arrival at: {kwargs['to']['city']} ({kwargs['to']['iataCode']}) \n"
                 f"Departure date: {kwargs['date']}"
        )
        print(message.status)

    def flight_not_found_notification(self):
        message = CLIENT.messages.create(
            from_="+19049005420",
            to="+917769932142",
            body=f"Sorry! The flight that you requested does not exist "
                 f"or has no recurring flights in the next 6 months."
        )
        print(message.status)
