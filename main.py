import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv


load_dotenv()
lat=os.environ.get("LAT")
lon=os.environ.get("LON")
appid=os.environ.get("OWM_API_KEY")
url=os.environ.get("OWM_API_ENDPOINT")
twilio_whatsapp=os.environ.get("TWILIO_WHATSAPP")
to_phone_whatsapp=os.environ.get("TO_PHONE_WHATSAPP")
twilio_ac_id=os.environ.get("TWILIO_AC_ID")
twilio_auth_token=os.environ.get("TWILIO_AUTH_TOKEN")
to_phone=os.environ.get("TO_PHONE")
twilio_phone=os.environ.get("TWILIO_PHONE")


parameters = {
    "lat":lat,
    "lon":lon,
    "appid":appid,
    "cnt":4
}


response = requests.get(url=url, params=parameters)
response.raise_for_status
weather_data = response.json()
# print(weather_data)
will_rain = False
for item in weather_data["list"]:
    condition_code = item["weather"][0]["id"]
    if int(condition_code) < 600:
        will_rain = True

if will_rain:
    client= Client(twilio_ac_id, twilio_auth_token)
    message = client.messages \
        .create(
            body="It's raining carry an umbrella!!!",
            from_=twilio_phone,
            to=to_phone,
        )
       
print(message.status)    

