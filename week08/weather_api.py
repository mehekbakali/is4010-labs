import requests


class WeatherAPI:
    def __init__(
        self,
        api_key,
        base_url="https://api.weatherapi.com/v1",
    ):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    def get_current_weather(self, location):
        try:
            response = requests.get(
                f"{self.base_url}/current.json",
                params={"key": self.api_key, "q": location},
                timeout=10,
            )
            response.raise_for_status()
            return response.json()
        except (requests.exceptions.RequestException, ValueError):
            return None

    def get_forecast(self, location, days=3):
        if days < 1 or days > 3:
            raise ValueError("Forecast days must be between 1 and 3.")

        try:
            response = requests.get(
                f"{self.base_url}/forecast.json",
                params={
                    "key": self.api_key,
                    "q": location,
                    "days": days,
                },
                timeout=10,
            )
            response.raise_for_status()
            return response.json()
        except (requests.exceptions.RequestException, ValueError):
            return None


def format_current_weather(data):
    location = data["location"]
    current = data["current"]

    city = location["name"]
    country = location["country"]
    temp = current["temp_f"]
    condition = current["condition"]["text"]

    return f"{city}, {country}: {temp}°F, {condition}"


def format_forecast(data):
    forecast_days = data["forecast"]["forecastday"]
    results = []

    for day in forecast_days:
        date = day["date"]
        forecast = day["day"]
        high = forecast["maxtemp_f"]
        low = forecast["mintemp_f"]
        condition = forecast["condition"]["text"]

        results.append(
            f"{date}: high {high}°F, low {low}°F, {condition}"
        )

    return "\n".join(results)
