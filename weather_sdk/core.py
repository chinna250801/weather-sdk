import requests
from weather_sdk.utils import WeatherAPIUtils


class WeatherSDK:
    _isinstance = None

    def __new__(cls, api_key):
        if cls._isinstance is None:
            cls._isinstance = super().__new__(cls)
            cls._isinstance.api_key = api_key

        return cls._isinstance

    def get_current_weather(self, city):
        params = {
            "q": city,
            "appid": self.api_key
        }
        url = WeatherAPIUtils.build_url("weather", params)
        response = requests.get(url)
        return WeatherAPIUtils.handle_response(response)

    def get_forecast(self, city, days):
        params = {
            "q": city,
            "cnt": days * 8,  # Each day has 8 data points (3-hour intervals)
            "appid": self.api_key
        }
        url = WeatherAPIUtils.build_url("forecast", params)
        response = requests.get(url)
        return WeatherAPIUtils.handle_response(response)






