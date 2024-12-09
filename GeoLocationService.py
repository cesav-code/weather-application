import requests

from Models import GeoLocation


class GeoLocationService:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/find"

    def fetch_city_data(self, city: str):
        params = {
            "q": city,
            "appid": self.api_key,
            "limit": 1,
        }
        try:
            response = requests.get(self.base_url, params=params)
            if response.status_code == 200:
                data = response.json()
                if "list" in data and data["list"]:
                    city_info = data["list"][0]
                    return {
                        "city": city_info["name"],
                        "lat": city_info["coord"]["lat"],
                        "lon": city_info["coord"]["lon"],
                        "country": city_info["sys"]["country"],
                    }
            return None
        except Exception as e:
            print(f"Error fetching data for {city}: {e}")
            return None

    def get_geolocation(self, cities: list):
        geolocations = []
        # ideally, we need an API that returns the latitude and longitude of all the given cities in one API call,
        # along with more specific details such as the postal code.
        for city in cities:
            city_data = self.fetch_city_data(city)
            if city_data:
                geo_location = GeoLocation(
                    city=city_data["city"],
                    lat=city_data["lat"],
                    lon=city_data["lon"],
                    country=city_data["country"],
                )
                geolocations.append(geo_location)
        return geolocations
