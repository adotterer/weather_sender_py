import requests
import json
import os
from dotenv import load_dotenv

load_dotenv("./.env")
API_KEY = os.environ.get("OPEN_WEATHER_API_KEY")

# print(API_KEY)
response = requests.get(
    f"https://api.openweathermap.org/data/2.5/onecall?lat=48&lon=-122&cnt=5&exlude=minutely,hourly&appid={API_KEY}"
)

with open("./json/weather.json", "w") as outfile:
    json.dump(response.json(), outfile)
