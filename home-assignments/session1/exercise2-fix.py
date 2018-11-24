import urllib.request
import requests
import json


def get_location_from_api():
    with urllib.request.urlopen("http://ip-api.com/json") as url:
        data = json.loads(url.read().decode())
        city = data["city"]
        country = data["country"]
    return city, country


def get_weather_from_api(city, country):
    api_key = "9c8b160816fc48b0288a6136e0989b2a"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city + ", " + country
    response = requests.get(complete_url)
    data = response.json()
    description = data["weather"][0]["main"]
    temperature = data["main"]["temp"]
    temperature -= 272.15
    return description, temperature


def write_to_file(text_file, city, country, description, temperature):
    print("The weather in {}, {} is {} and the temperature is {:.02f} °C".format(
            city, country, description, temperature), file=text_file)


cities_dict = {
    "Buenos Aires": "Argentina",
    "Kigali": "Rwanda",
    "Cali": "Colombia",
    "Tokyo": "Japan",
    "Delhi": "India",
    "Guatemala City": "Guatemala",
    "Prague": "Czech Republic",
    "Oslo": "Norway",
    "Abuja": "Nigeria",
    "Cancun": "Mexico"
}


def main():
    with open("weather_report.txt", "w") as text_file:
        city, country = get_location_from_api()
        description, temperature = get_weather_from_api(city, country)
        write_to_file(text_file, city, country, description, temperature)
        for city, country in cities_dict.items():
            description, temperature = get_weather_from_api(city, country)
            write_to_file(text_file, city, country, description, temperature)


if __name__ == '__main__':
    main()
