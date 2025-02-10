import requests
from typing import Any


class getWeather:

    def __init__(self):
        pass

    def get_weather(self, location: str) -> dict[str, Any]:
        '''
        Makes a request to aws EC2 server to make the api call and return a json/dictionary of the weather data in the given location.
        
        Return type contains nested dictionaries and lists with str type keys
        Example return value structure:
            {
    "location": {
        "name": "New York",
        "region": "New York",
        "country": "United States of America",
        "lat": 40.7142,
        "lon": -74.0064,
        "tz_id": "America/New_York",
        "localtime_epoch": 1735354653,
        "localtime": "2024-12-27 21:57"
    },
    "current": {
        "last_updated_epoch": 1735353900,
        "last_updated": "2024-12-27 21:45",
        "temp_c": 5.1,
        "temp_f": 41.2,
        "is_day": 0,
        "condition": {
            "text": "Partly cloudy",
            "icon": "//cdn.weatherapi.com/weather/64x64/night/116.png",
            "code": 1003
        }, ...
        '''
        EC2_URL = 'http://ec2-3-129-211-177.us-east-2.compute.amazonaws.com:8000/weather'

        try:
            payload = {
                'location' : location
            }

            response = requests.post(EC2_URL, json=payload)
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.RequestException as e:
            print(f'Request error occured: {e}')
            return None
        
    def parse_weather(self, weather: dict) -> tuple[str, str, str, str, str, str, str, str, str, str, str]:
        '''
        Parses weather dictionary from API and returns extracted data.
        Params: Expects json that is returned from API call made in get_weather.
        '''
        # Checking if api actually returned data
        if weather is None:
            raise ValueError('Check that location is valid and try again')
        else:
            location = weather.get('location', {})
            current =  weather.get('current', {})
            condition = current.get('condition', {})

            # Retreiving items from dictionary returned from API and returning them as a tuple
            name, region = location.get('name', 'Unknown'), location.get('region', 'Unknown')
            country = location.get('country', 'Unknown')
            text = condition.get('text', 'Unknown condition') 
            icon = condition.get('icon', 'Icon unavailable')
            
            # Imperial data
            temp_f = current.get('temp_f', 'Unknown temp' )
            feelslike_f = current.get('feelslike_f', 'Unknown')
            wind_mph = current.get('wind_mph', 'Wind speed unknown')

            # Metric data
            temp_c = current.get('temp_c', 'Unknown temp')
            feelslike_c =  current.get('feelslike_c', 'Unknown')
            wind_kph = current.get('wind_kph', 'Wind speed unknown')

            return name, region, country, text, icon, temp_f, feelslike_f, wind_mph, temp_c, feelslike_c, wind_kph
        
if __name__ == '__main__':
    weather = getWeather()
    print(weather.get_weather('New york'))