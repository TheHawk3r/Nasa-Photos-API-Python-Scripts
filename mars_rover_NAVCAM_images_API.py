import requests

endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
api_key = "DEMO_KEY"
params = {"earth_date":"2021-03-15","camera":"NAVCAM", "api_key":api_key}

response = requests.get(endpoint, params)
photos = response.json()["photos"]

image_sources = [item["img_src"] for item in photos]

print(image_sources)

