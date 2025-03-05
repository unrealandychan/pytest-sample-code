import requests

def get_weather(city):
    response = requests.get(f"https://api.weather.com/v1/{city}")
    if response.status_code != 200:
        raise ValueError(f"Unable to get weather for {city}")
    else:
        return response.json()