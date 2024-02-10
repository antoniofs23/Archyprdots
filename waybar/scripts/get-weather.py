#!/usr/bin/env python

import json
import requests
from datetime import datetime

WEATHER_CODES = {
    '113': '☀️ ',
    '116': '⛅ ',
    '119': '☁️ ',
    '122': '☁️ ',
    '143': '☁️ ',
    '176': '🌧️',
    '179': '🌧️',
    '182': '🌧️',
    '185': '🌧️',
    '200': '⛈️ ',
    '227': '🌨️',
    '230': '🌨️',
    '248': '☁️ ',
    '260': '☁️ ',
    '263': '🌧️',
    '266': '🌧️',
    '281': '🌧️',
    '284': '🌧️',
    '293': '🌧️',
    '296': '🌧️',
    '299': '🌧️',
    '302': '🌧️',
    '305': '🌧️',
    '308': '🌧️',
    '311': '🌧️',
    '314': '🌧️',
    '317': '🌧️',
    '320': '🌨️',
    '323': '🌨️',
    '326': '🌨️',
    '329': '❄️ ',
    '332': '❄️ ',
    '335': '❄️ ',
    '338': '❄️ ',
    '350': '🌧️',
    '353': '🌧️',
    '356': '🌧️',
    '359': '🌧️',
    '362': '🌧️',
    '365': '🌧️',
    '368': '🌧️',
    '371': '❄️',
    '374': '🌨️',
    '377': '🌨️',
    '386': '🌨️',
    '389': '🌨️',
    '392': '🌧️',
    '395': '❄️ '
}

data = {}


weather = requests.get("https://wttr.in/?for:wqmat=j1").json()


def format_time(time):
    return time.replace("00", "").zfill(2)


def format_temp(temp):
    return (hour['FeelsLikeF']+"°").ljust(3)


def format_chances(hour):
    chances = {
        "chanceoffog": "Fog",
        "chanceoffrost": "Frost",
        "chanceofovercast": "Overcast",
        "chanceofrain": "Rain",
        "chanceofsnow": "Snow",
        "chanceofsunshine": "Sunshine",
        "chanceofthunder": "Thunder",
        "chanceofwindy": "Wind"
    }

    conditions = []
    for event in chances.keys():
        if int(hour[event]) > 0:
            conditions.append(chances[event]+" "+hour[event]+"%")
    return ", ".join(conditions)

tempint = int(weather['current_condition'][0]['FeelsLikeF'])
extrachar = ''
if tempint > 0 and tempint < 10:
    extrachar = '+'


data['text'] = ' '+WEATHER_CODES[weather['current_condition'][0]['weatherCode']] + \
    " "+extrachar+weather['current_condition'][0]['FeelsLikeF']+"°"

data["tooltip"] = f"Feels like: {weather['current_condition'][0]['FeelsLikeF']}°\n"
data["tooltip"] += f"Wind: {weather['current_condition'][0]['windspeedKmph']}Km/h\n"
data["tooltip"] += f"Humidity: {weather['current_condition'][0]['humidity']}%\n"
data["tooltip"] += f"Cloud Cover: {weather['current_condition'][0]['cloudcover']}%\n"
data["tooltip"] += f"Latitude: {weather['nearest_area'][0]['latitude']}\n"
data["tooltip"] += f"Moon-phase: {weather['weather'][0]['astronomy'][0]['moon_phase']}\n"
data["tooltip"] += f"Moon-illumination: {weather['weather'][0]['astronomy'][0]['moon_illumination']}%\n"
data["tooltip"] += f"Moonrise: {weather['weather'][0]['astronomy'][0]['moonrise']}\n"


print(json.dumps(data))
