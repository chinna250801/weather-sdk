from weather_sdk.core import WeatherSDK


class WeatherFactory:
    @classmethod
    def create_sdk(cls, api_key):
        return WeatherSDK(api_key)
