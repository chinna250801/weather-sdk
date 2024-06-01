import unittest
from unittest.mock import patch, MagicMock
from weather_sdk.core import WeatherSDK
from weather_sdk.utils import WeatherAPIUtils


class TestWeatherSDK(unittest.TestCase):

    @patch('weather_sdk.core.requests.get')
    @patch.object(WeatherAPIUtils, 'build_url')
    @patch.object(WeatherAPIUtils, 'handle_response')
    def test_get_current_weather(self, mock_handle_response, mock_build_url, mock_requests_get):
        # Mock data
        mock_response_data = {
            "weather": [{"description": "clear sky"}],
            "main": {"temp": 298.77}
        }

        # Setup the mocks
        mock_handle_response.return_value = mock_response_data
        mock_requests_get.return_value = MagicMock(status_code=200)

        sdk = WeatherSDK("fake_api_key")
        result = sdk.get_current_weather("San Francisco")

        # Check if the build_url method was called with the correct arguments
        mock_build_url.assert_called_with("weather", {"q": "San Francisco", "appid": "fake_api_key"})

        # Check if the result matches the expected output
        self.assertEqual(result["weather"][0]["description"], "clear sky")
        self.assertEqual(result["main"]["temp"], 298.77)

    @patch('weather_sdk.core.requests.get')
    @patch.object(WeatherAPIUtils, 'build_url')
    @patch.object(WeatherAPIUtils, 'handle_response')
    def test_get_forecast(self, mock_handle_response, mock_build_url, mock_requests_get):
        # Mock data
        mock_response_data = {
            "list": [
                {"dt_txt": "2023-06-01 12:00:00", "main": {"temp": 298.77}},
                {"dt_txt": "2023-06-01 15:00:00", "main": {"temp": 300.55}}
            ]
        }

        # Setup the mocks
        mock_handle_response.return_value = mock_response_data
        mock_requests_get.return_value = MagicMock(status_code=200)

        sdk = WeatherSDK("fake_api_key")
        result = sdk.get_forecast("San Francisco", 1)

        # Check if the build_url method was called with the correct arguments
        mock_build_url.assert_called_with("forecast", {"q": "San Francisco", "cnt": 8, "appid": "fake_api_key"})

        # Check if the result matches the expected output
        self.assertEqual(len(result["list"]), 2)
        self.assertEqual(result["list"][0]["main"]["temp"], 298.77)


