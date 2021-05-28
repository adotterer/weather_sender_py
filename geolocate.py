from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="weather_sender")


def find_coordinates(location):
    geolocation = geolocator.geocode(location)
    response = {"latitude": geolocation.latitude,
                "longitude": geolocation.longitude}
    print(geolocation.raw["display_name"])
    return response


find_coordinates("Lake Kachess, WA")
