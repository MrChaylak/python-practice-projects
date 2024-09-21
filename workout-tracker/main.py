import requests
from datetime import datetime
import os
from dotenv import load_dotenv

GENDER = os.getenv("MyGender")
WEIGHT_KG = os.getenv("MyWeight")
HEIGHT_CM = os.getenv("MyHeight")
AGE = os.getenv("MyAge")

load_dotenv("C:/PyNotes/.env")
APP_ID = os.getenv("MyNutritionAppID")
API_KEY = os.getenv("MyNutritionApiKey")
BEARER_TOKEN = os.getenv("MySheetBearerToken")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.getenv("MySheetEndPoint")

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
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
# print(result)

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

    # sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    # Bearer Token Authentication
    bearer_headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )
