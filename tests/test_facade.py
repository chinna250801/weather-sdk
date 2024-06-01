import unittest
from unittest.mock import patch, MagicMock
from weather_sdk.facade import WeatherFacade


class TestWeatherFacade(unittest.TestCase):

    @patch('weather_sdk.facade.WeatherFactory.create_sdk')
    def test_get_current_weather(self, mock_create_sdk):
        # Mock the SDK instance returned by the factory
        mock_sdk_instance = MagicMock()
        mock_create_sdk.return_value = mock_sdk_instance

        # Mock the return value of the get_current_weather method
        mock_sdk_instance.get_current_weather.return_value = {
            "weather": [{"description": "clear sky"}],
            "main": {"temp": 298.77}
        }

        facade = WeatherFacade("your_api_key")
        result = facade.get_current_weather("San Francisco")

        # Check if the result matches the expected output
        self.assertEqual(result["weather"][0]["description"], "clear sky")
        self.assertEqual(result["main"]["temp"], 298.77)

        # Ensure the get_current_weather method was called with the correct argument
        mock_sdk_instance.get_current_weather.assert_called_with("San Francisco")

    @patch('weather_sdk.facade.WeatherFactory.create_sdk')
    def test_get_forecast(self, mock_create_sdk):
        # Mock the SDK instance returned by the factory
        mock_sdk_instance = MagicMock()
        mock_create_sdk.return_value = mock_sdk_instance

        # Mock the return value of the get_forecast method
        mock_sdk_instance.get_forecast.return_value = {
            "list": [
                {"dt_txt": "2023-06-01 12:00:00", "main": {"temp": 298.77}},
                {"dt_txt": "2023-06-01 15:00:00", "main": {"temp": 300.55}}
            ]
        }

        facade = WeatherFacade("your_api_key")
        result = facade.get_forecast("San Francisco", 2)

        # Check if the result matches the expected output
        self.assertEqual(len(result["list"]), 2)
        self.assertEqual(result["list"][0]["main"]["temp"], 298.77)

        # Ensure the get_forecast method was called with the correct arguments
        mock_sdk_instance.get_forecast.assert_called_with("San Francisco", 2)

