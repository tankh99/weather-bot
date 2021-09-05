import os
import requests

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}"
def get_weather(area):
    url = f"{BASE_URL}&q={area}"
    response = requests.get(url)
    if response.status_code == 401:
        return Exception("Unauthorised API Key")
        
    return response.json()
    


