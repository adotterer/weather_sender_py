import requests
import json
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv("./.env")
API_KEY = os.environ.get("OPEN_WEATHER_API_KEY")

# print(API_KEY)
# response = requests.get(
#     f"https://api.openweathermap.org/data/2.5/onecall?lat=48&lon=-122&cnt=5&exclude=minutely,hourly&appid={API_KEY}"
# )

# json_data = response.json()

# with open("./json/weather.json", "w") as outfile:
#     json.dump(json_data, outfile, indent=4)

weather_dict = json.load(open("./json/weather.json", "r"))

# print(weather_dict["daily"])


month_dict = {
    "01": "Jan",
    "02": "Feb",
    "03": "Mar",
    "04": "Apr",
    "05": "May",
    "06": "Jun",
    "07": "Jul",
    "08": "Aug",
    "09": "Sep",
    "10": "Oct",
    "11": "Nov",
    "12": "Dec"
}


def k_to_fah(kalvin_temp):
    return round(9/5 * (kalvin_temp - 273.15) + 32)


for day in weather_dict["daily"]:
    [_year, _month, _day] = datetime.utcfromtimestamp(
        day['dt']).strftime('%Y-%m-%d').split("-")

    day_temp = k_to_fah(day["temp"]["day"])
    pretty_date = f'{month_dict[_month]} {_day} {_year}'

    print(pretty_date)
    print(day_temp)
    print("------")


# y = json.loads(json_data)
# print(json_data["daily"])
