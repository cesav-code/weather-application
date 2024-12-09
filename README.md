# FastAPI Weather Application

This is a FastAPI application that provides weather-related services. It allows you to retrieve weather data for cities, visualize weather metrics, and download weather data in CSV format.

## Features

- **Get weather data for a list of cities**: Fetch the weather information such as temperature, wind speed, and humidity for given cities.
- **Get geolocation information**: Fetch latitude, longitude, and other geolocation details of given cities.
- **Download weather data as CSV**: Download weather data for cities in CSV format with options to sort the data.
- **Visualize weather data**: Generate plots based on weather data, allowing visualizations for temperature, wind speed, or humidity.

## Requirements

To install the required dependencies and create new env, use the following command:

```bash
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

To run the application use below command
```bash
uvicorn main:app --reload
```

# API definitions

## Fetches weather data for the given cities.

GET [/weather](http://127.0.0.1:8000/weather)

Query Parameters:
cities : list of cities (comma separated)

Body
```bash
{
    "cities": [
        "London",
        "Paris",
        "Berlin"
    ]
}
```
Example response
```bash
[
  { "city": "London", "temperature": 7.4, "wind_speed": 21.0, "humidity": 12 },
  { "city": "Paris", "temperature": 7.1, "wind_speed": 13.5, "humidity": 21 },
  { "city": "Berlin", "temperature": 3.8, "wind_speed": 11.2, "humidity": 32 }
]
```

## Fetches geolocation (latitude, longitude, country, etc.) for the given cities.

GET [/geolocation](http://127.0.0.1:8000/geolocation)

Query Parameters:
cities : list of cities (comma separated)

Body
```bash
{
    "cities": [
        "London",
        "Paris",
        "Berlin"
    ]
}
```
Example response
```bash
[
    {
        "city": "London",
        "lat": 51.5085,
        "lon": -0.1257,
        "country": "GB"
    },
    {
        "city": "Paris",
        "lat": 48.8534,
        "lon": 2.3488,
        "country": "FR"
    },
    {
        "city": "Berlin",
        "lat": 52.5244,
        "lon": 13.4105,
        "country": "DE"
    }
]
```

## Download Weather Data as CSV

Downloads weather data for cities as a CSV file. You can sort the data by a specific field.

Query Parameters:

cities: List of cities (comma separated)
sort_by: Field to sort by (optional). Default is "Temperature (C)". Possible values: "City", "Country", "Temperature (C)", "Temperature (F)", "Humidity (%)", "Wind Speed (m/s)", "Wind Speed (mph)".
ascending: Boolean to indicate sorting order. Default is True (ascending order).


GET [/download_weather_csv](http://127.0.0.1:8000/download_weather_csv?sort_by=City&ascending=true)

Example response CSV
```bash
City,Country,Temperature (C),Temperature (F),Humidity (%),Wind Speed (m/s),Wind Speed (mph)
London,GB,7.1,44.78,12,18.4,41.159696
Mumbai,IN,26.9,80.42,21,13.3,29.751302000000003
Paris,FR,5.8,42.44,32,13.8,30.869772000000005
```

## Visualize Weather Data

Visualizes the weather data in a plot image. The plot can be based on temperature, wind speed, or humidity.

Query Parameters:

cities: List of cities (comma separated)
visualized_by: Field to visualize by. Possible values: "temperature", "wind_speed", "humidity". Default is temperature.

GET [/weather_visualization](http://127.0.0.1:8000/weather_visualization?visualized_by=temperature)

Example response Image:

![image](https://github.com/user-attachments/assets/a2cd3811-bbc2-4bc2-a0ea-eeafbd8b266e)


