# prints weather for location from command line

APPID = ''  # your api id here
import json
import requests
import sys

# get cma argument location
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()
location = ''.join(sys.argv[1:])

# Download JSON Data from OpenWeatherMap.org
url = f'https://api.openweathermap.org/data/2.5/forecast/daily?q={location}&cnt=3&APPID={APPID}'
response = requests.get(url)
response.raise_for_status()

# Uncomment to view raw json text:
# print(response.text)

# Load json data into python var
weatherData = json.loads(response.text)

# print weather
w = weatherData['list']
print(f'Current weather in {location}:')
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
