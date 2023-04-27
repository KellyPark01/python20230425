import requests

# fetch data from the API
response = requests.get('https://randomuser.me/api/?results=20')
data = response.json()

# iterate over the results and extract the information
for result in data['results']:
    # extract the first and last name
    first_name = result['name']['first']
    last_name = result['name']['last']
    
    # extract the street name
    street_name = result['location']['street']['name']
    
    # output the result
    print(f"{first_name} {last_name} lives on {street_name}")
