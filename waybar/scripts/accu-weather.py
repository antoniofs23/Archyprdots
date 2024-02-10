import re
import json
import requests
from bs4 import BeautifulSoup

"""
Scrape personal accuweather link with your city/zip-code
"""


# scrape weather data
def ScrapeWeather(
    target_url="https://www.accuweather.com/en/us/homestead/33030/current-weather/337544",
):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }

    resp = requests.get(target_url, headers=headers).text
    soup = BeautifulSoup(resp, "html.parser")

    weatherInfo = soup.find_all("div", {"class": "current-weather-details"})

    # clean the scraped data using regular expressions
    # the "<.*?>" removes html tags
    patterns = ["<.*?>", "\n", "®", "°", "%", "™"]

    # to remove multiple patterns need to use the "|" or regex pipe
    cleanedInfo = re.sub("|".join(patterns), "", str(weatherInfo))

    # now we just want the numbers which we can get from regular expressions yet again
    mesurements = re.findall(r"\d+", cleanedInfo)
    # now lets define a dictionary with all the info we want
    try:
        MeasurementDict = {
            "weather": mesurements[0] + "°F",
            "DewPoint": mesurements[7] + "°F",
            "Humidity": mesurements[5] + "%",
            "Visibility": mesurements[11] + " mi",
            "Cloud Coverage": mesurements[10] + "%",
        }
    except IndexError:
        MeasurementDict = {
            "weather": mesurements[0] + "°F",
            "DewPoint": mesurements[5] + "°F",
            "Humidity": mesurements[3] + "%",
            "Visibility": mesurements[9] + " mi",
            "Cloud Coverage": mesurements[8] + "%",
        }

    return MeasurementDict


weather = ScrapeWeather()
data = {}
data["text"] = f"{weather['weather']}"
data["tooltip"] = f"Dew Point: {weather['DewPoint']}\n"
data["tooltip"] += f"Humidity: {weather['Humidity']}\n"
data["tooltip"] += f"Visibility: {weather['Visibility']}\n"
data["tooltip"] += f"Cloud Coverage: {weather['Cloud Coverage']}\n"

print(json.dumps(data))
