import json

import requests

# data for singapore
response = requests.get("https://www.metaweather.com/api/location/1062617/")

data = response.text

jsondata = json.loads(data)

currentTemp = jsondata['consolidated_weather'][0]['the_temp']

if currentTemp > 30:
    print("Bring a cap! Temperature is:", currentTemp)
elif currentTemp > 20:
    print("Wear T-Shirt and Shorts. Temperature is:", currentTemp)
elif currentTemp > 10:
    print("Wear a light jacket. Temperature is:", currentTemp)
elif currentTemp > 0:
    print("Wear a thick jacket. Temperature is:", currentTemp)
elif currentTemp > -10:
    print("Wear multiple layers. Temperature is:", currentTemp)
elif currentTemp > -20:
    print("Wear a parka. Temperature is:", currentTemp)
else:
    print("You shouldn't be outside. Temperature is:", currentTemp)

