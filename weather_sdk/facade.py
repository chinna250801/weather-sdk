from weather_sdk.factory import WeatherFactory


class WeatherFacade:
    def __init__(self, api_key):
        self.sdk = WeatherFactory.create_sdk(api_key)

    def get_current_weather(self, city):
        return self.sdk.get_current_weather(city)

    def get_forecast(self, city, days):
        return self.sdk.get_forecast(city, days)


