# Weather SDK

## Overview
This Weather SDK provides a simple interface for accessing weather data from the OpenWeatherMap API. It allows you to retrieve current weather conditions, weather forecasts, and historical weather data for a specified location.

## Features
- Get current weather conditions for a specific location.
- Retrieve weather forecasts for the next several days.

## Installation
To install the Weather SDK, you can use pip:
```bash
pip install weather-sdk
```

## Usage
Initializing the SDK

First, import and initialize the SDK with your OpenWeatherMap API key:
```python 
from weather_sdk.facade import WeatherFacade

api_key = "your_openweathermap_api_key"
weather = WeatherFacade(api_key)
```

## Fetching Current Weather
Fetch current weather data for a specific city:

```python
city = "London"
current_weather = weather.get_current_weather(city)
print(current_weather)
```

## Fetching Weather Forecast

Fetch weather forecast data for a specific city and number of days:

```python
city = "London"
days = 5
forecast = weather.get_forecast(city, days)
print(forecast)
```

## Example Output

Here's an example of what the output might look like when fetching current weather:

```json
{
  "coord": {"lon": -0.1257, "lat": 51.5085},
  "weather": [
    {"id": 800, "main": "Clear", "description": "clear sky", "icon": "01d"}
  ],
  "base": "stations",
  "main": {
    "temp": 288.55,
    "feels_like": 287.13,
    "temp_min": 287.04,
    "temp_max": 290.15,
    "pressure": 1023,
    "humidity": 56
  },
  "visibility": 10000,
  "wind": {"speed": 3.09, "deg": 70},
  "clouds": {"all": 0},
  "dt": 1622890820,
  "sys": {
    "type": 2,
    "id": 2019646,
    "country": "GB",
    "sunrise": 1622874378,
    "sunset": 1622932296
  },
  "timezone": 3600,
  "id": 2643743,
  "name": "London",
  "cod": 200
}

```
