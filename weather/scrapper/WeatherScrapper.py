import requests
import json

UNIQUE_KEY = '5b5df8201186c63f630bf72087e5a378'
URL = ' https://api.openweathermap.org/data/2.5/weather'
UNITS = ('metric', 'imperial')
FILE_NAME = 'city.list.json'

class WeatherScrapper:

    @classmethod
    def get_weather(cls, city_name='', units=''):
        if not city_name:
            raise ValueError("City name can't be empty!")
        if units not in UNITS:
            raise ValueError(f"No temperature units called {units}")
        r = requests.get(URL, params={'appid': UNIQUE_KEY, 'q': city_name, 'units': units})
        print(r.json())
        return r.json()

    @classmethod
    def __get_cities_json(cls):
        with open(FILE_NAME) as f:
            res = json.load(f)
            return res

if __name__ == '__main__':
    WeatherScrapper.get_weather(city_name='Kharkiva', units='metric')
