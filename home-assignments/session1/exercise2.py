"""
Guy home assignment 2 in coding 1 session 1

1. Check my location according to my IP
   Check current weather at my location using weather API
   Write result to text file format
2. Create a list with 10 cities
   Print their current weather in format
   “The weather in <city>, <country>(full country name) is XX degrees"
"""

import urllib.request
import requests
import json

with urllib.request.urlopen("http://ip-api.com/json") as url:
    data = json.loads(url.read().decode())
    city = data["city"]
    country = data["country"]
    print(data)
    print(city + " , " + country)

def get_weather(city):
    api_key = "9c8b160816fc48b0288a6136e0989b2a"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    x = response.json()
    y = x["main"]
    current_temperature = y["temp"]
    current_temperature -= 272.15
    current_pressure = y["pressure"]
    current_humidiy = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]
    return current_temperature, current_pressure, current_humidiy, weather_description

current_temperature, current_pressure, current_humidiy, weather_description = get_weather(city)

with open("weather.txt", "w") as text_file:
    print(" Temperature (in celsius unit) = " +
          str(current_temperature) +
          "\n Atmospheric pressure (in hPa unit) = " +
          str(current_pressure) +
          "\n Humidity (in percentage) = " +
          str(current_humidiy) +
          "\n Description = " +
          str(weather_description), file=text_file)
    print(f"weather_description: {weather_description}", file = text_file)

cities_dict = {
    "buenos aires": "argentina",
    "kigali": "rwanda",
    "cali": "colombia",
    "tokyo": "japan",
    "delhi": "india",
    "guatemala city": "guatemala",
    "prague": "czech republic",
    "oslo": "norway",
    "Abuja": "nigeria",
    "cancun": "mexico"
}

for city in cities_dict:
    country = cities_dict[city]
    current_temperature, _, _, _ = get_weather(city)
    print(f"The weather in {city}, {country} is {current_temperature:.02f} degrees")

