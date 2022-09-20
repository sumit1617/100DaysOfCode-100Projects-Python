# Response from the website can be in numeric code
# 1XX : Hold on
# 2XX : Here You Go
# 3XX : Go Away
# 4XX : You Screwed Up
# 5XX : I Screwed Up


import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (f"latitude = {latitude}", f"longitude = {longitude}")
print(iss_position)
