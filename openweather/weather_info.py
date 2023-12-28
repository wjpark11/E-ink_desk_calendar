from dotenv import load_dotenv
import os

import requests

load_dotenv()
WEATHER_API_KEY = os.getenv("OPEN_WEATHER_MAP_API_KEY")


def get_weather_info(lat: float, lon: float) -> dict:
    api_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}"
    response = requests.get(api_url)

    print(response.json())


if __name__ == "__main__":
    get_weather_info(37.5665, 126.9780)
