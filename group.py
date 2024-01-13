import censusgeocode as cg
import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv() 
mapbox_token = os.environ['MAPBOX_TOKEN']

#example address 
address = "2600 Benjamin Franklin Pkwy, Philadelphia, PA 19130"

#make request to mapboxapi using requests module to get longitude and latitude for address
url = "https://api.mapbox.com/geocoding/v5/mapbox.places/" + address + ".json?access_token=" + mapbox_token

response = requests.get(url).json()

#extract longitude and latitude from response
longitude = response["features"][0]["geometry"]["coordinates"][0]
latitude = response["features"][0]["geometry"]["coordinates"][1]

#make request to censusgeocode api using censusgeocode module to get census tract for address
cg_result = cg.coordinates(x=longitude, y=latitude)

#pull block group from cg_result
block_group = cg_result["2020 Census Blocks"][0]["BLOCK"]
