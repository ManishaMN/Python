import pprint
import requests
import sys
from datetime import datetime
from statistics import mean
import csv

#city and country hard coded
loc = ['Guilin, China', 'Dissen, Germany', 'Guatemala City, Guatemala', 'Kandukur, India', 'Nanaimo, British Columbia',	'Uijeongbu-si, South Korea',
          'Yangon, Myanmar', 'Jalpa de Mendez, Mexico',	'Enugu, Nigeria', 'Peterhead, Scotland', 'Lima, Peru', 'Singapore, Singapore', 'Kaohsiung, Taiwan',
          'Grimesland, North Carolina',	'Visalia, California',	'Colonia del Sacramento, Uruguay']

# API Key
api_key = 'key'
cities_temp = []

# lat long and api output for all locations
for i in range(len(loc)):
    URL = 'http://api.openweathermap.org/geo/1.0/direct'
    city = loc[i]
    city_itr = loc[i]
    # print(city_itr)
    geo = f'{URL}?q={city}&limit=5&appid={api_key}'
    resp = requests.get(geo)

    if resp.status_code != 200:  # Failure?
        print(f'Error geocoding {city}: {resp.status_code}')
        sys.exit(1)

    if len(resp.json()) == 0:  # No such city?
        print(f'Error locating city {city}; {resp.status_code}')
        sys.exit(2)
    json = resp.json()

    if type(json) == list:  # List of cities?
        lat = json[0]['lat']
        lon = json[0]['lon']
    else:  # Unknown city?
        print(f'Error, invalid data returned for city {city}, {resp.status_code}')
        sys.exit(3)

    URL = 'http://api.openweathermap.org/data/2.5/forecast'
    forecast = f'{URL}?lat={lat}&lon={lon}&appid={api_key}'
    resp = requests.get(forecast)

    if resp.status_code != 200:  # Failure?
        print(f'Error retrieving data: {resp.status_code}')
        sys.exit(4)

    data = resp.json()

#lopping through 40 blocks

    # finding 00:00:00 block
    for i in range(40):
        if datetime.strptime(data['list'][i]['dt_txt'], '%Y-%m-%d %H:%M:%S').time().strftime("%H:%M:%S") == '00:00:00':
            # print(i)
            start = i
            break

    # calculating min and max temp
    city = []
    for x in range(4):
        min_t = []
        max_t = []
        day = []
        for i in range(start, start+8):
            min_t.append(data['list'][i]['main']['temp_min'])
            max_t.append(data['list'][i]['main']['temp_max'])
        city.append((min(min_t)))
        city.append((max(max_t)))
        # print(city)
        max(max_t)
        start = start + 8

    #calculating average min and max temp
    avg_min = []
    avg_max = []
    for x in range(0, len(city), 2):
        avg_min.append(city[x])
    avg_min_temp = mean(avg_min)

    for x in range(1, len(city), 2):
        avg_max.append(city[x])
    avg_max_temp = mean(avg_max)
    city.append(avg_min_temp)
    city.append(avg_max_temp)
    # print(city)

    #func celsius to kelvin
    def celsius_kelvin(x):
        return x - 273.15

    # func to decimals
    def decimals(x):
        return "{:.2f}".format(x)

    city_celsius = list(map(celsius_kelvin, city))
    city_celsius = list(map(decimals, city_celsius))

    city_celsius.insert(0, city_itr) #inserting city name
    cities_temp.append(city_celsius) #appending temperatures

#adding headers and creating output file
header_list = ['City','Min 1','Max 1','Min 2','Max 2','Min 3','Max 3','Min 4','Max 4','Min Avg','Max Avg']
output_file = open('temp.csv', 'w+', newline='')

#exporting temp.csv
with output_file:
    head = csv.DictWriter(output_file, delimiter=',', fieldnames=header_list)
    head.writeheader()
    write = csv.writer(output_file)
    write.writerows(cities_temp)





