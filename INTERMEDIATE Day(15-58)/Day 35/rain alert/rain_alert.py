import requests
from twilio.rest import Client



api_key = ""
MY_LAT = 19.075983
MY_LONG = 72.877655
account_sid = ""
auth_token = ""
phone_no = "+12184504653"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}


response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hours_data in weather_slice:
    condition_code = hours_data["weather"][0]["id"]
    if int(condition_code) <= 1000:
        will_rain = True

if will_rain:

    client = Client(account_sid, auth_token)
    message = client.messages.create(body="Hello kaisa hai bhai!! msg aaya kya??😁😇\n\nTera bhai Sumit London se 😆",
                                     from_="+12184504653", to="+918433766575")
    print(message.status)
