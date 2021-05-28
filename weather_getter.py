import requests
import json
import os
from dotenv import load_dotenv
from datetime import datetime
from pytz import timezone

pacific = timezone('US/Pacific')
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
        day['dt']).strftime('%Y-%m-%d %H:%M:%S %Z%z').split("-")

    high = k_to_fah(day["temp"]["max"])
    low = k_to_fah(day["temp"]["min"])
    day_temp = k_to_fah(day["temp"]["day"])
    night_temp = k_to_fah(day["temp"]["night"])
    fl_day_temp = k_to_fah(day["feels_like"]["day"])
    fl_night_temp = k_to_fah(day["feels_like"]["night"])
    pretty_date = f'{month_dict[_month]} {_day} {_year}'
    sunrise = datetime.utcfromtimestamp(day["sunrise"])

    # print(datetime.utctimestamp(sunrise).strftime("%H:%M:%S %Z%"))

    # print(pacific.localize(sunrise.astimezone(pacific)).strftime(fmt))
    # sunset =

    # print(f' {pretty_date} '.center(34, "="))
    # print("High".ljust(28, "."), str(high).rjust(5))
    # print("Low".ljust(28, "."), str(low).rjust(5))
    # print("Day".ljust(28, "."), str(day_temp).rjust(5))
    # print("Night".ljust(28, "."), str(night_temp).rjust(5))
    # print("Feels like day".ljust(28, "."), str(fl_day_temp).rjust(5))
    # print("Feels like night".ljust(28, "."), str(fl_night_temp).rjust(5))
    # print("      ")
    # sunrise time

    


# y = json.loads(json_data)
# print(json_data["daily"])
