from dotenv import load_dotenv
import requests
import datetime
import os


load_dotenv()
GENDER = os.getenv("GENDER")
WEIGHT_KG = os.getenv("WEIGHT_KG")
HEIGHT_CM = os.getenv("HEIGHT_CM")
AGE = os.getenv("AGE")

EXERCISE_APP_ID = os.getenv("EXERCISE_APP_ID")
EXERCISE_API_KEY = os.getenv("EXERCISE_API_KEY")
SHEETY_AUTH_TOKEN = os.getenv("SHEETY_AUTH_TOKEN")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")


# -----------------GET EXERCISE STATS-----------------

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_prompt = input("Tell me which exercises you did: ")        # Example: "I ran 5km for 30 min"

exercise_headers = {
    "x-app-id": EXERCISE_APP_ID,
    "x-app-key": EXERCISE_API_KEY
}
exercise_body = {
    "query": exercise_prompt,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

exercise_response = requests.post(url=exercise_endpoint, json=exercise_body, headers=exercise_headers)
exercises_json = exercise_response.json()
print(exercise_response)
print(exercises_json)

# -----------------GET ROW-----------------

# get_sheety_endpoint = SHEETY_ENDPOINT
# sheety_response = requests.get(url=get_sheety_endpoint)
# print(sheety_response.json())

# -----------------POST ROW-----------------

post_sheety_endpoint = SHEETY_ENDPOINT

today_date = datetime.datetime.now().strftime("%d/%m/%Y")
today_time = datetime.datetime.now().time().strftime("%H:%M:%S")
exercise = exercises_json['exercises'][0]['name'].title()
duration = exercises_json['exercises'][0]['duration_min']
calories = exercises_json['exercises'][0]['nf_calories']

sheety_body = {
    'workout': {
        "date": today_date,
        "time": today_time,
        "exercise": exercise,
        "duration (min)": duration,
        "calories": calories
    }
}

sheety_headers = {
  "Authorization": SHEETY_AUTH_TOKEN
}

sheety_response = requests.post(url=post_sheety_endpoint, json=sheety_body, headers=sheety_headers)
print(sheety_response)
print(sheety_response.json())

# -----------------PUT ROW-----------------

# -----------------DELETE ROW-----------------

