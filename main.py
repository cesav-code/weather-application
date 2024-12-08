from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from dotenv import load_dotenv
from fastapi import Query
from AppView import process_weather_data
from GeoLocationService import GeoLocationService
from Models import CityList
from WeatherService import WeatherService
import os
import io
from visualize_weather_data import plot_weather_data

load_dotenv()
api_key = os.getenv("OPEN_WEATHER_MAP_API_KEY")
app = FastAPI()

geo_service = GeoLocationService(api_key)
weather_service = WeatherService()


@app.get("/")
async def root():
    return {"message": "Hii Singular"}


@app.get("/weather")
async def weather(cities: CityList):
    # It will return weather related data for given cities

    # First we will get lat long got all the cities and then we will get weather info, from lat long.
    geolocations = geo_service.get_geolocation(cities.cities)

    return weather_service.fetch_bulk_weather(geolocations)


@app.get("/geolocation")
async def geolocation(cities: CityList):
    geolocations = geo_service.get_geolocation(cities.cities)
    return geolocations


@app.get("/download_weather_csv")
async def download_weather_csv(
        cities: CityList,
        sort_by: str = Query(
            "Temperature (C)", regex="^(City|Country|Temperature \(C\)|Temperature \(F\)|Humidity \(%\)|Wind Speed \(m/s\)|Wind Speed \(mph\))$"),
        ascending: bool = Query(True)):

    # We will get weather information csv file here. and also we can get that data in sorted order for given field in
    # query params

    geolocations = geo_service.get_geolocation(cities.cities)
    weather_data_list = weather_service.fetch_bulk_weather(geolocations)

    # Data frame
    df = process_weather_data(weather_data_list)
    # Sorted data
    df_sorted = df.sort_values(by=sort_by, ascending=ascending)

    output = io.StringIO()
    df_sorted.to_csv(output, index=False)

    output.seek(0)

    # CSV file
    return StreamingResponse(output, media_type="text/csv",
                             headers={"Content-Disposition": "attachment; filename=weather_data.csv"})


@app.get("/weather_visualization")
async def download_weather_csv(
        cities: CityList,
        visualized_by: str = Query('temperature', enum=['temperature', 'wind_speed', 'humidity'])):

    # We can visualize data based on 'temperature', 'wind_speed' and 'humidity'

    geolocations = geo_service.get_geolocation(cities.cities)
    weather_data_list = weather_service.fetch_bulk_weather(geolocations)

    try:
        image_stream = plot_weather_data(weather_data_list, visualized_by)
    except ValueError as e:
        return {"error": str(e)}

    return StreamingResponse(image_stream, media_type="image/png", headers={"Content-Disposition": "attachment; filename=weather_data_plot.png"})
