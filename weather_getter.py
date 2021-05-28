import requests
import json
import os
from dotenv import load_dotenv
from pytz import timezone
from datetime import datetime
from geolocate import find_coordinates
from month_dict import month_dict
from emoji_dict import emoji_dict
import re
weather_dict = json.load(open("./json/weather.json", "r"))

pacific = timezone('US/Pacific')
load_dotenv("./.env")

API_KEY = os.environ.get("OPEN_WEATHER_API_KEY")


def k_to_fah(kalvin_temp):
    return round(9/5 * (kalvin_temp - 273.15) + 32)


def writeMemo(target_location="Lake Kachess, WA"):
    # TODO: dynamic input of location to find weather
    location_dict = find_coordinates(target_location)

    latitude, longitude, name = location_dict.values()
    # strip name of united states
    name = re.sub(r", United States", " 🌈", name)

    # comment back in to get current weather ~
    # |
    # |
    # v
    # response = requests.get(
    #     f"https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&cnt=5&exclude=minutely,hourly&appid={API_KEY}"
    # )

    # json_data = response.json()

    # with open("./json/weather.json", "w") as outfile:
    #     json.dump(json_data, outfile, indent=4)
    #
    # ~ end ~
    memo = open(f"./memos/daily.txt", "w")
    memo.write("")

    for day in weather_dict["daily"]:
        [year, month, calday] = datetime.utcfromtimestamp(
            day['dt']).strftime('%Y-%m-%d %H:%M:%S %Z%z').split("-")

        high = k_to_fah(day["temp"]["max"])
        low = k_to_fah(day["temp"]["min"])
        day_temp = k_to_fah(day["temp"]["day"])
        night_temp = k_to_fah(day["temp"]["night"])
        fl_day_temp = k_to_fah(day["feels_like"]["day"])
        fl_night_temp = k_to_fah(day["feels_like"]["night"])
        [day_of_month, _byebye] = calday.split()
        [weather] = day["weather"]
        _id, forecast, forecast_description, icon = weather.values()

        [_date, sunrise_timestamp] = str(datetime.fromtimestamp(
            day["sunrise"], tz=pacific)).split()
        [sunrise_time, _notsure] = sunrise_timestamp.split("-")

        [_date, sunset_timestamp] = str(datetime.fromtimestamp(
            day["sunset"], tz=pacific)).split()
        [sunset_time, _notsure] = sunset_timestamp.split("-")

        pretty_date = f'{month_dict[month]} {day_of_month} {year}'

        if forecast not in emoji_dict:
            print("adding to emoji dict")
            emoji_dict[forecast] = "✌️"[0:1]

        memo = open(f"./memos/daily.txt", "a+")
        memo.write(f' {pretty_date} '.center(26, emoji_dict[forecast]) + "\n")
        memo.write(name.center(20) + "\n")
        memo.write("\n \t" + f'forecast: {forecast_description} ' + "\n")
        memo.write(f'🌅 Sunrise: {sunrise_time} ' + "🌄".ljust(2, "🌄") + "\n")

        # print(name.center(20))
        # print("\n \t", f'forecast: {forecast_description} ', "\n")

        # print(f' Sunrise: {sunrise_time} '.rjust(12, "🌅"), "🌄".ljust(6, "🌄"))
        memo.write("High".ljust(24, ".") + str(high).rjust(2))
        memo.write('\n')
        memo.write("Low".ljust(24, ".") + str(low).rjust(2))
        memo.write('\n')
        memo.write("Day".ljust(24, ".") + str(day_temp).rjust(2))
        memo.write('\n')
        memo.write("Feels like day".ljust(24, ".") + str(fl_day_temp).rjust(2))
        memo.write('\n')
        memo.write(f'🌌 Sunset: {sunset_time} ' + "🌠".ljust(2, "🌠"))
        memo.write('\n')
        memo.write("Night".ljust(24, ".") + str(night_temp).rjust(2))
        memo.write('\n')
        memo.write("Feels like night".ljust(
            24, ".") + str(fl_night_temp).rjust(2))
        memo.write("\n")
        memo.write("\n")
