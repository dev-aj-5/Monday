import requests


GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


def get_weather(prompt):

    city = prompt.lower()

    city = city.replace("weather", "")
    city = city.replace("in", "")
    city = city.strip()

    if not city:
        return "Please specify a city."

    try:

        # -------------------------
        # Find coordinates
        # -------------------------

        geo = requests.get(
            GEOCODE_URL,
            params={
                "name": city,
                "count": 1
            },
            timeout=10
        )

        geo.raise_for_status()

        results = geo.json().get("results")

        if not results:
            return "I couldn't find that city."

        location = results[0]

        latitude = location["latitude"]
        longitude = location["longitude"]

        # -------------------------
        # Current Weather
        # -------------------------

        weather = requests.get(
            WEATHER_URL,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m,wind_speed_10m"
            },
            timeout=10
        )

        weather.raise_for_status()

        current = weather.json()["current"]

        return (
            f"🌤 Weather in {location['name']}\n\n"
            f"🌡 Temperature: {current['temperature_2m']}°C\n"
            f"💨 Wind Speed: {current['wind_speed_10m']} km/h"
        )

    except Exception as e:

        return f"Weather Error:\n{e}"