import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

lat=os.environ.get("LAT")
lon=os.environ.get("LON")
appid=os.environ.get("OWM_API_KEY")
url=os.environ.get("OWM_API_ENDPOINT")
twilio_whatsapp=os.environ.get("TWILIO_WHATSAPP")
to_phone=os.environ.get("TO_PHONE")

parameters = {
    "lat":lat,
    "lon":lon,
    "appid":appid,
    "cnt":4
}


response = requests.get(url=url, params=parameters)
response.raise_for_status
weather_data = response.json()
