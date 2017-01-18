import json
from twilio.rest import TwilioRestClient



def send_sms(message, recipient):

    with open('./creds.json') as f:
        creds = json.load(f)

    ACCOUNT_SID = creds["sid"]
    AUTH_TOKEN = creds["token"]

    twilio_number = creds["from"]

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    # number format -> '+12223334444'
    message = client.messages.create(
    to=recipient,
    from_=twilio_number,
    body=message,
    )
