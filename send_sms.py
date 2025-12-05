import requests
from config import MELI_API_KEY, SMS_SENDER, SMS_RECEIVER


def send_sms(text):
    if not MELI_API_KEY:
        raise ValueError("MELIPAYAMAK_API_KEY is not set")

    url = "https://console.melipayamak.com/api/send/simple/" + MELI_API_KEY

    payload = {
        "from": SMS_SENDER,
        "to": SMS_RECEIVER,
        "text": text
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()

    return response.json()
