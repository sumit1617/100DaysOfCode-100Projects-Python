#Note! For the code to work you need to replace all the placeholders with
#Your own details. e.g. account_sid, lat/lon, from/to phone numbers.

import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall?"
api_key = os.environ.get("1a92241f5bda60443e9725d4df1fc3db")
account_sid = "AC80ddae257c3e0f8308aee28e19824b9c"
auth_token = os.environ.get("dded1434248b2e60c9b48efcf8a89ec5")
MY_LAT = 19.075983
MY_LONG = 72.877655

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 1000:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+12184504653",
        to="+918433766575"
    )
    print(message.status)




# api_key = "1a92241f5bda60443e9725d4df1fc3db"
# MY_LAT = 19.075983
# MY_LONG = 72.877655
# account_sid = "AC80ddae257c3e0f8308aee28e19824b9c"
# auth_token = "dded1434248b2e60c9b48efcf8a89ec5"
# phone_no = "+12184504653"