"""
A script that returns images 
from the nasa rover
Spirit using the NasaApi.
"""
from datetime import date, timedelta
import os
import requests
import shutil

endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/spirit/photos"
api_key = "DEMO_KEY"
# Earth_date variables.
today = date.today()
yesterday = date(today.year, today.month, today.day - 1).isoformat() 
two_days_ago = date(today.year, today.month, today.day - 2).isoformat()
date = '2004-09-09'
# Define parameters for the endpoint.
params = {"earth_date":date, "api_key":api_key} 

# Request a response from the api.
response = requests.get(endpoint, params)
# Save the response in json format and only the photos entries.
photos = response.json()["photos"]

# Save all img_src key values in a list using a for loop.
image_sources = [item["img_src"] for item in photos]

print(image_sources)

# Start downloading the images in a seperate directory

directory = f"Spirit {date}"
os.mkdir(directory)
directory_path = os.path.join(os.getcwd(), directory)

print(f"Image directory created {directory}")

for img_src in image_sources:
    img_url = img_src
    filename = img_url.split("/")[-1]
    complete_path = os.path.join(directory_path, filename)
    img_request = requests.get(img_url, stream = True)

    if img_request.status_code == 200:
        img_request.decode_content = True

        with open(complete_path, 'wb') as f:
            shutil.copyfileobj(img_request.raw, f)

        print("Image Succesfully Downloaded: ", filename)
    else:
        print("Image Couldn't be retreived")
