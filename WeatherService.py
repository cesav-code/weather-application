import requests

from Models import GeoLocation, WeatherData


class WeatherService:

    def __init__(self):
        self.base_url = "https://api.open-meteo.com/v1/forecast"

    def fetch_bulk_weather(self, locations: list[GeoLocation]):

        latitudes = ",".join(str(location.lat) for location in locations)
        longitudes = ",".join(str(location.lon) for location in locations)

        params = {
            "latitude": latitudes,
            "longitude": longitudes,
            "current_weather": "true",
        }

        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            weather_data_list = []
            data = response.json()
            if isinstance(data, list):
                for idx, item in enumerate(data):
                    current_weather = item.get("current_weather", {})
                    location = locations[idx]  # GeoLocation object
                    weather_data = WeatherData(location=location, temperature=current_weather.get(
                        "temperature"), wind_speed=current_weather.get("windspeed"), humidity=current_weather.get("humidity", None))
                    weather_data_list.append(weather_data)
            else:
                print(f"Unexpected data format: {data}")

            return weather_data_list
        else:
            print(
                f"Error: Unable to fetch weather data (HTTP {response.status_code})")
            return None
