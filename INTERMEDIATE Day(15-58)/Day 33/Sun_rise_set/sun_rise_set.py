import requests
from datetime import *


MY_LAT = 19.280430
MY_LONG = 72.847900

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}


response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
time = (f"sunrise = {sunrise}", f"sunset = {sunset}")
print(time)


time_now = datetime.now()
print(time_now)
