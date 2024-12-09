from pydantic import BaseModel
from typing import List


class CityList(BaseModel):
    cities: List[str]


class GeoLocation:
    def __init__(self, city: str, lat: float, lon: float, country: str):
        self.city = city
        self.lat = lat
        self.lon = lon
        self.country = country

    def to_dict(self):
        return {
            "city": self.city,
            "lat": self.lat,
            "lon": self.lon,
            "country": self.country,
        }


class WeatherData:
    def __init__(self, location: GeoLocation, temperature: float, wind_speed: float, humidity: int):
        self.location = location
        self.temperature = temperature
        self.wind_speed = wind_speed
        self.humidity = humidity

    def to_dict(self):
        return {
            "temperature": self.temperature,
            "wind_speed": self.wind_speed,
            "humidity": self.humidity,
            "location": self.location.to_dict()
        }
