class WeatherAPIUtils:
    @staticmethod
    def build_url(endpoint, params):
        """
        Constructs the full URL for the API request.

        :param endpoint: API endpoint (e.g., "weather" or "forecast")
        :param params: Dictionary of query parameters
        :return: Full URL as a string
        """
        base_url = "http://api.openweathermap.org/data/2.5/"
        url = base_url + endpoint
        query_string = "&".join([f"{key}={value}" for key, value in params.items()])
        return f"{url}?{query_string}"

    @staticmethod
    def handle_response(response):
        """
        Handles the API response, raising an error for bad requests.

        :param response: Response object from the requests library
        :return: JSON data from the response if the request was successful
        """
        response.raise_for_status()  # Raise an error for HTTP codes 400 or above
        return response.json()
