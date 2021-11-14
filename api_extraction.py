#Uses the OpenWeatherMap API to extract data and then returns it to be used elsewhere.

import requests
import config



def weather_temp(city):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(city, config.api_key)
    r = requests.get(url)
    results = r.json()

    return results['main']['temp']

