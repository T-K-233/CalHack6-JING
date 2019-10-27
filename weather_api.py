""" weather_api.py

Fetch the local weather data using coordinates.
"""

import json

import requests

def getWeather():
    res = requests.get("https://api.darksky.net/forecast/68b57c294028ea3886af9e58b329b435/37.8715,-122.2730")
    data = json.loads(res.text)
    json.dump(data, open("data.json", "w", encoding="utf-8"))
    data = {
        "temperatureMin": int(data["daily"]["data"][0]["temperatureMin"]),
        "temperatureMax": int(data["daily"]["data"][0]["temperatureMax"]),
        "text": data["daily"]["data"][0]["summary"]
        }
    data["voice"] = "Today's weather is {0}. Maximum temperature's around {1}Fahrenheit.".format(data["text"], data["temperatureMax"])
    return data
