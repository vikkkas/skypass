from twilio.rest import Client

TWILIO_SID = 'AC1cf2f37c15db1be031a4697423f293ed'
TWILIO_AUTH_TOKEN = '3f76c8c876c781c6e0ecb3062c5ef600'
TWILIO_VIRTUAL_NUMBER = '+19034596533'
TWILIO_VERIFIED_NUMBER = '+919824250512'

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
