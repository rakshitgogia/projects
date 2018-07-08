import json
import requests
import sys


def convertToFarenheit(currentTemp):
    convertedTemp = currentTemp * 9 / 5 + 32
    return convertedTemp

# location details of Singapore
latitude = 1.29
longitude = 103.85
queryLocation = "https://www.metaweather.com/api/location/search/?lattlong=" + str(latitude) + "," + str(longitude)
locationData = requests.get(queryLocation).text
jsonLocationData = json.loads(locationData)
id = jsonLocationData[0]['woeid']
cityName = jsonLocationData[0]['title']
print ("You are in:", cityName)

queryData = "https://www.metaweather.com/api/location/"+ str(id) + "/"
data = requests.get(queryData).text

jsonData = json.loads(data)

currentTemp = jsonData['consolidated_weather'][0]['the_temp']
outputTemp = currentTemp
units = 'C'
if len(sys.argv) == 2:
    units = sys.argv[1]

if units == 'F':
    outputTemp = convertToFarenheit(currentTemp)

if currentTemp > 30:
    print("Bring a cap! Temperature is:", outputTemp)
elif currentTemp > 20:
    print("Wear T-Shirt and Shorts. Temperature is:", outputTemp)
elif currentTemp > 10:
    print("Wear a light jacket. Temperature is:", outputTemp)
elif currentTemp > 0:
    print("Wear a thick jacket. Temperature is:", outputTemp)
elif currentTemp > -10:
    print("Wear multiple layers. Temperature is:", outputTemp)
elif currentTemp > -20:
    print("Wear a parka. Temperature is:", outputTemp)
else:
    print("You shouldn't be outside. Temperature is:", outputTemp)
