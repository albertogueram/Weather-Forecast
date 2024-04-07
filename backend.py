import requests

OW_url = "https://api.openweathermap.org/data/2.5/forecast"


def get_data(lat=40.416775, lon=-3.703790, cnt=8):
    parameters = {
        "lat": lat,
        "lon": lon,
        "appid": "a8e424506e66ffa5776feda004e00efa",
        "cnt": cnt,
        "lang": "es"
    }
    response = requests.get(OW_url, params=parameters)
    weather_data = response.json()
    filtered_weather_data = weather_data["list"]
    for i in filtered_weather_data:
        print(i["dt_txt"])
        print(i["weather"][0]["description"])

    return filtered_weather_data

get_data()

