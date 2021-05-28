from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="weather_sender")


def find_coordinates(location):
    print(location)
    geolocation = geolocator.geocode(("175 5th Avenue NYC"))
    response = {"latitude": geolocation.latitude,
                "longitude": geolocation.longitude}

    return response
