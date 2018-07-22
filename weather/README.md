# weather
By Rakshit Gogia

Version 1.0, 22nd July 2018

Weatherman detects your location and tells you what to wear based on the weather.
Deciding what to wear is a daily struggle and Weatherman helps you out with that.

## Requirements:
You need to have requests (http://docs.python-requests.org/en/master/) and geocoder (https://pypi.org/project/geocoder/1.0.0/) installed

## Usage:
python3 weather.py \[options]

### options:

> default: Weatherman detects your location based on your IP address and tells you what to wear based on the weather

> -s, --search "<city name>": Weatherman searches for the city you entered
 and tells residents of that city what to wear

> -u, --units <C/ F>: Gives you output in Celsius or Farenheit depending
on the option you provided (default is Celsius)

### examples:

```
python3 weather.py
You are in: Singapore
Wear T-Shirt and Shorts. Temperature is: 29.76 C
```

```
python3 weather.py -s Melbourne
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

