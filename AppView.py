import pandas as pd
from MathsHelper import celsius_to_fahrenheit, mps_to_mph


# Create data frame
def process_weather_data(weather_data_list):
    processed_data = []

    for weather_data in weather_data_list:
        city = weather_data.location.city
        country = weather_data.location.country
        temperature_celsius = weather_data.temperature
        wind_speed_mps = weather_data.wind_speed
        humidity = weather_data.humidity
        temperature_fahrenheit = celsius_to_fahrenheit(
            temperature_celsius) if temperature_celsius is not None else None
        wind_speed_mph = mps_to_mph(
            wind_speed_mps) if wind_speed_mps is not None else None

        processed_data.append({
            "City": city,
            "Country": country,
            "Temperature (C)": temperature_celsius,
            "Temperature (F)": temperature_fahrenheit,
            "Humidity (%)": humidity,
            "Wind Speed (m/s)": wind_speed_mps,
            "Wind Speed (mph)": wind_speed_mph
        })

    df = pd.DataFrame(processed_data)

    return df
