import requests
from datetime import datetime
import smtplib
import time

my_email = "sumitkumarsingh1817@gmail.com"
password = "sumit@1806"
MY_LAT = 19.280430  # Your Latitude
MY_LONG = 72.847900  # Your Longitude


# If the ISS is close to my current position
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude >= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude >= MY_LONG + 5:
        return True


# and it is currently dark
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


# Send mail when ISS is overhead.
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="ss5933070@gmail.com",
            msg="Subject:Look Up!!!!!!\n\nThe ISS is above you in the sky."
        )

# BONUS: run the code every 60 seconds.
