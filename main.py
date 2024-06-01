from weather_sdk.facade import WeatherFacade

# Replace 'your_api_key' with the actual API key you copied from OpenWeatherMap
api_key = "d30877f2392af71102752193750ae9da"

sdk = WeatherFacade(api_key=api_key)

# Get current weather
current_weather = sdk.get_current_weather("ayodhya")
print(current_weather)

# Get weather forecast for 5 days
forecast = sdk.get_forecast("delhi", 5)
print(forecast)

