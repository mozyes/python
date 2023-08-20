import requests
from datetime import datetime

GENDER = "male"
WEIGHT = 71
HEIGHT = 174
AGE = 30

APP_ID = "your id here"
APP_KEY = "your api key here"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/061723e72a00a4cb416518b1801c23ea/copyOfMyWorkout/workouts"

exercise_text = input("Which exercises you did? ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

bearer_headers = {
    "Authorization": "your bearer token here"
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
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

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)
