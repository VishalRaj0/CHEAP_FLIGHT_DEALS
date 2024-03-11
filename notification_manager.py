from twilio.rest import Client

ACCOUNT_SID = "YOUR TWILIO ACCOUNT SID"
AUTH_TOKEN = "YOUR TWILIO AUTHORIZATION TOKEN"
TWILIO_NUMBER = ""
RECIEVER_NUMBER = ""

CLIENT = Client(ACCOUNT_SID, AUTH_TOKEN)
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_notification(self, **kwargs):
        message = CLIENT.messages.create(
            from_=TWILIO_NUMBER,
            to=RECIEVER_NUMBER,
            body=f"Price: EUR {kwargs['price']} \n"
                 f"Departure from: {kwargs['city_from']} ({kwargs['city_code_from']}) \n"
                 f"Arrival at: {kwargs['to']['city']} ({kwargs['to']['iataCode']}) \n"
                 f"Departure date: {kwargs['date']}"
        )
        print(message.status)

    def flight_not_found_notification(self):
        message = CLIENT.messages.create(
            from_=TWILIO_NUMBER,
            to=RECIEVER_NUMBER,
            body=f"Sorry! The flight that you requested does not exist "
                 f"or has no recurring flights in the next 6 months."
        )
        print(message.status)
