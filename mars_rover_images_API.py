"""A script that returns images from the nasa rovers 
(Curiosity, Oportuniy and Spirit) using the NasaApi.
"""

from datetime import date, timedelta
import requests

endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
api_key = "DEMO_KEY"
# Earth_date variables.
today = date.today()
yesterday = date(today.year, today.month, today.day -1).isoformat() 
two_days_ago = date(today.year, today.month, today.day -2).isoformat()
# Define parameters for the endpoint.
params = {"earth_date":two_days_ago, "api_key":api_key} 

# Request a response from the api.
response = requests.get(endpoint, params)
# Save the response in json format and only the photos entries.
photos = response.json()["photos"]

# Save all img_src key values in a list using a for loop.
image_sources = [item["img_src"] for item in photos]

print(image_sources)

