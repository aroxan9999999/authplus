import random
import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()
code = {}


def send_sms(phone_number, message):
    client = Client("{os.getenv('TWILO_USERNAME')}", '{os.getenv("TWILO_PASSWORD")}')
    message = client.messages.create(
        body=message,
        from_='{os.getenv("TWILO_NUMBER")}',
        to=phone_number
    )
    return message.sid


def generate_code():
    codde = random.randint(1000, 9999)
    while codde in code.keys():
        generate_code()
    return codde
