import os
import requests

def get_weather(city: str = "New York") -> dict:
    """Fetch current weather data for the given city from OpenWeather API.

    Parameters
    ----------
    city: str
        Name of the city to query.

    Returns
    -------
    dict
        Parsed JSON response containing weather information.
    """
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENWEATHER_API_KEY environment variable not set")

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    weather = get_weather("New York")
    print(weather)
