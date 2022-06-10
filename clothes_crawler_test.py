from aiohttp import Payload
import googlemaps
import requests
import json
import pandas as pd

google_key=''
gmaps = googlemaps.Client(key=google_key)

buisness_list=[]

location = (25.039071256441673, 121.50992871392059)
distance = 3000
keywords = '服飾'
lang = 'zh-tw'
resp = gmaps.places_nearby(
    location = location,
    keyword = keywords,
    radius = distance,
    language = lang
)

buisness_list.extend(resp.get('results'))
print(buisness_list)

df = pd.DataFrame(buisness_list)
new_df = df.dropna()
print(new_df)
#df.to_csv('clothes_shop_zz.csv',index=False)
