import requests
import json

url=r"http://api.openweathermap.org/data/2.5/forecast?id=3582677&APPID=8fc532fa1fa981e1237c5ce9ed510080&units=imperial"

# connect to url. GET
response=requests.get(url)

# check if connection is
if response.json()['cod']=='200':
    # get data part from response
    data_json=response.text
    # parse the JSON data
    data=json.loads(data_json)
    # get location data
    location_data=data["city"]
    # get weather data
    weather_data=data["list"]
    # print location and country
    print("Location: ",location_data["name"])
    print("Country : ",location_data["country"])
    # print present weather conditions
    # get last from the weather data list
    present_weather_data=weather_data[len(weather_data)-1]
    # print current conditions
    print("Current temperature            : ",present_weather_data["main"]["temp"])
    print("Current feels like temperature : ",present_weather_data["main"]["feels_like"])
    print("Current weather                : ",present_weather_data["weather"][0]["main"])
    for day_data in weather_data:
        print(day_data["dt_txt"]," - ","High ", day_data["main"]["temp_max"],", Low ", day_data["main"]["temp_min"], day_data["weather"][0]["main"])
