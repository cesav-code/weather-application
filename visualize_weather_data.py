import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import io


def plot_weather_data(weather_data_list, visualize_by):
    cities = [weather_data.location.city for weather_data in weather_data_list]

    # Extract relevant data based on 'visualize_by'
    if visualize_by == 'temperature':
        data = [weather_data.temperature for weather_data in weather_data_list]
        y_label = 'Temperature (°C)'
        title = 'City-wise Temperatures'
    elif visualize_by == 'wind_speed':
        data = [weather_data.wind_speed for weather_data in weather_data_list]
        y_label = 'Wind Speed (m/s)'
        title = 'City-wise Wind Speeds'
    elif visualize_by == 'humidity':
        data = [weather_data.humidity if weather_data.humidity is not None else 0 for weather_data in
                weather_data_list]  # Handle None values
        y_label = 'Humidity (%)'
        title = 'City-wise Humidity Levels'
    else:
        raise ValueError(
            "Invalid 'visualize_by' parameter. Use 'temperature', 'wind_speed', or 'humidity'.")

    df = pd.DataFrame({
        'City': cities,
        visualize_by.capitalize(): data
    })

    sns.set_palette("viridis")
    plt.figure(figsize=(8, 5))
    sns.barplot(x='City', y=visualize_by.capitalize(), data=df)

    plt.xlabel("City")
    plt.ylabel(y_label)
    plt.title(title)

    image_stream = io.BytesIO()
    plt.savefig(image_stream, format='png')
    plt.close()
    image_stream.seek(0)
    return image_stream
