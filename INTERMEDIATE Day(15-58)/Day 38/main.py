import requests
from datetime import datetime

API_ID = "20a1bb8b"
API_KEY = "dbe951a76b7fc15639291bea51b2b660"


GENDER = "Male"
WEIGHT_KG = "85"
HEIGHT_CM = "182"
AGE = "19"


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/17d07ad88ed2cdfffc2590245d2a3552/workoutTracking/sheet1"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    print(sheet_inputs)
    print(sheet_response.text)

