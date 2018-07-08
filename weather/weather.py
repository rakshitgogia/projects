import json
import requests
import sys
import geocoder





class Weatherman:
    latitude = 0
    longitude = 0
    currentTemp = 0
    outputTemp = 0
    units = 'C'

    def convertToFarenheit(currentTemp):
        convertedTemp = currentTemp * 9 / 5 + 32
        return round(convertedTemp, 2)

    def readData():
        g = geocoder.ip('me')
        latlon = g.latlng

        # city = geocoder.google("moscow")
        # latlon = city.southwest
        Weatherman.latitude = latlon[0]
        Weatherman.longitude = latlon[1]
        queryLocation = "https://www.metaweather.com/api/location/search/?lattlong=" + str(Weatherman.latitude) + "," + str(
            Weatherman.longitude)
        locationData = requests.get(queryLocation).text
        jsonLocationData = json.loads(locationData)
        id = jsonLocationData[0]['woeid']
        cityName = jsonLocationData[0]['title']
        print("You are in:", cityName)
        queryData = "https://www.metaweather.com/api/location/" + str(id) + "/"
        data = requests.get(queryData).text

        jsonData = json.loads(data)

        Weatherman.currentTemp = jsonData['consolidated_weather'][0]['the_temp']
        Weatherman.outputTemp = Weatherman.currentTemp

    def printOutput():
        if len(sys.argv) == 2:
            Weatherman.units = sys.argv[1]

        if Weatherman.units == 'F':
            Weatherman.outputTemp = Weatherman.convertToFarenheit(Weatherman.currentTemp)

        if Weatherman.currentTemp > 30:
            print("Bring a cap! Temperature is:", Weatherman.outputTemp, Weatherman.units)
        elif Weatherman.currentTemp > 20:
            print("Wear T-Shirt and Shorts. Temperature is:", Weatherman.outputTemp, Weatherman.units)
        elif Weatherman.currentTemp > 10:
            print("Wear a light jacket. Temperature is:", Weatherman.outputTemp, Weatherman.units)
        elif Weatherman.currentTemp > 0:
            print("Wear a thick jacket. Temperature is:", Weatherman.outputTemp, Weatherman.units)
        elif Weatherman.currentTemp > -10:
            print("Wear multiple layers. Temperature is:", Weatherman.outputTemp, Weatherman.units)
        elif Weatherman.currentTemp > -20:
            print("Wear a parka. Temperature is:", Weatherman.outputTemp, Weatherman.units)
        else:
            print("You shouldn't be outside. Temperature is:", Weatherman.outputTemp, Weatherman.units)

Weatherman.readData()
Weatherman.printOutput()