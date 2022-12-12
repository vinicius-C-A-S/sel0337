from requests import get
import json
from pprint import pprint
#from haversine import haversine

stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

my_lat = -28.95078
my_lon = -49.468256

#all_stations = get(stations).json()['items']

#def find_closest():
    #smallest = 20036
    #for station in all_stations:
        #station_lat = station['weather_stn_lat']
        #station_lon = station['weather_stn_long']
        #distance = haversine(my_lon, my_lat, station_lon, station_lat)
        #if distance < smallest:
            #smallest = distance
            #closest_station = station['weather_stn_id']
    #return closest_station

#closest_station = station['966583']        
closest_stn = 966583        

weather = weather + str(closest_stn)

UFSC_weather = get(weather).json()['items']
pprint(UFSC_weather)

#def find_closest():
    #smallest = 20036
    #for station in all_stations:
       # print(station)