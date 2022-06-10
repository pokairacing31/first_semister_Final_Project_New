from aiohttp import Payload
import googlemaps
import requests
import json
import pandas as pd

google_key=''
gmaps = googlemaps.Client(key=google_key)

buisness_list=[]

location = (25.095633351994202, 121.54520939350584)
distance = 2000
keywords = '服飾'
lang = 'zh-tw'
resp = gmaps.places_details(
    location = location,
    keyword = keywords,
    radius = distance,
    language = lang
)

buisness_list.extend(resp.get('results'))
print(buisness_list)
