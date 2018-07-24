# Weatherman
By Rakshit Gogia

Version 1.2, 23rd July 2018

Deciding what to wear is a daily struggle and Weatherman helps you out with that.
Weatherman detects your location and tells you what to wear based on the weather.

The weather data is sourced from MetaWeather's API - https://www.metaweather.com/api/

## Requirements:
You need to have the following installed:
- [python3](https://www.python.org/downloads/)

- [requests](http://docs.python-requests.org/en/master/)

- [geocoder](https://pypi.org/project/geocoder/1.0.0/)


## Usage:
python3 weather.py \[-h] \[-s <city name>] \[-u {C,F}]


### optional arguments:
```
  -h, --help            show this help message and exit
  -s "<city name>", --search "<city name>"
                        Weatherman searches for the city you entered and tells
                        residents of that city what to wear
  -u {C,F}, --units {C,F}
                        Gives you output in Celsius or Fahrenheit depending on
                        the option you provided (default is Celsius)
```
### examples:

```
python3 weather.py
You are in: Singapore
Wear T-Shirt and Shorts. Temperature is: 29.76 C
```

```
python3 weather.py -s "Melbourne"
You are in: Melbourne
Wear a light jacket. Temperature is: 12.41 C
```

```
python3 weather.py -u F
You are in: Singapore
Wear T-Shirt and Shorts. Temperature is: 85.57 F
```

```
python3 weather.py -u F --search "New Delhi"
You are in: New Delhi
Bring a cap! Temperature is: 88.05 F
```

