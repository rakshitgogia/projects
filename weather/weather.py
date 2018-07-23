import json
import requests
import geocoder
import argparse


class Weatherman:
    def __init__(self, units_in):
        self.units = units_in
        self.search_query = False
        self.connection_tries = 5

    def validate_input(self):
        parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                         description='Deciding what to wear is a daily struggle and '
                                                     'Weatherman helps you out with that.'
                                                     '\nWeatherman detects your location and tells you '
                                                     'what to wear based on the weather.')
        parser.add_argument('-s', '--search',
                            metavar='"<city name>"',
                            help='Weatherman searches for the city you entered '
                                 'and tells residents of that city what to wear')
        parser.add_argument('-u', '--units',
                            choices=['C', 'F'],
                            help='Gives you output in Celsius or Fahrenheit depending on the option you provided '
                                 '(default is Celsius)')
        args = parser.parse_args()
        if args.units:
            self.units = args.units
        if args.search:
            self.search_query = args.search

    def read_data(self):
        if not self.search_query:
            # get latitude and longitude from IP Address
            g = geocoder.ip('me')
            latlon = g.latlng
        else:
            # get latitude and longitude from search query
            latlon = self.get_search_query()
        self.latitude = latlon[0]
        self.longitude = latlon[1]
        # parse json data from API
        query_location = "https://www.metaweather.com/api/location/search/?lattlong=" + \
                        str(self.latitude) + "," + str(self.longitude)
        location_data = requests.get(query_location).text
        json_location_data = json.loads(location_data)
        id = json_location_data[0]['woeid']
        city_name = json_location_data[0]['title']
        print("You are in:", city_name)
        query_iD = "https://www.metaweather.com/api/location/" + str(id) + "/"
        id_data = requests.get(query_iD).text
        json_iDData = json.loads(id_data)
        self.current_temp = json_iDData['consolidated_weather'][0]['the_temp']

        if self.units == 'F':
            self.output_temp = self.convert_to_farenheit(self.current_temp)
        else:
            self.output_temp = self.current_temp
        # round to 2 decimal places
        self.output_temp = round(self.output_temp, 2)

    def print_output(self):
        # output what clothes to wear based on weather
        if self.current_temp > 30:
            print("Bring a cap! Temperature is:", self.output_temp, self.units)
        elif self.current_temp > 20:
            print("Wear T-Shirt and Shorts. Temperature is:", self.output_temp, self.units)
        elif self.current_temp > 10:
            print("Wear a light jacket. Temperature is:", self.output_temp, self.units)
        elif self.current_temp > 0:
            print("Wear a thick jacket. Temperature is:", self.output_temp, self.units)
        elif self.current_temp > -10:
            print("Wear multiple layers. Temperature is:", self.output_temp, self.units)
        elif self.current_temp > -20:
            print("Wear a parka. Temperature is:", self.output_temp, self.units)
        else:
            print("You shouldn't be outside. Temperature is:", self.output_temp, self.units)

    # helper functions
    def convert_to_farenheit(self, current_temp):
        self.converted_temp = current_temp * 9 / 5 + 32
        return round(self.converted_temp, 2)

    def get_search_query(self):
        try:
            # try to search 3 times
            for attempt in range(self.connection_tries):
                latlon = geocoder.google(self.search_query).southwest
                if latlon:
                    return latlon
            raise TypeError
        except TypeError:
            print("Invalid search query")
            exit(1)


# default is Celsius mode
my_weatherman = Weatherman('C')

my_weatherman.validate_input()
my_weatherman.read_data()
my_weatherman.print_output()
