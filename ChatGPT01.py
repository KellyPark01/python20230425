import requests
import csv

# Define the OpenStreetMap API endpoint and query parameters
url = 'https://nominatim.openstreetmap.org/search'
params = {
    'format': 'json',
    'limit': 100,
    'q': 'Paris, France'  # Change this to your desired location
}

# Send a GET request to the OpenStreetMap API endpoint with the query parameters
response = requests.get(url, params=params)

# Parse the JSON response into a list of dictionaries
results = response.json()

# Create a csv file and write the location information as rows
with open('location_info.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['Name', 'Latitude', 'Longitude'])
    # Write the location information as rows
    for result in results:
        name = result['display_name']
        lat = result['lat']
        lon = result['lon']
        writer.writerow([name, lat, lon])