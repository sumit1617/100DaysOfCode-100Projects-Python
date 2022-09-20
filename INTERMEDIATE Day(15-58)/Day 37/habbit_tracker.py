import requests
from datetime import datetime

TOKEN = "singh18sumit"
USERNAME = "sumit1806"


pixela_endpoint = "https://pixe.la/v1/users"

users_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Creating User
# response = requests.post(url=pixela_endpoint, json=users_params)
# print(response.text)

# Creating a Graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "Hr",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

entry_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime(year=2022, month=4, day=26)
entry_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "8"
}


put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20220426"
put_config = {
    "quantity": "6"
}

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20220426"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)