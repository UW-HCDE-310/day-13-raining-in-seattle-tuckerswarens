import urllib.request
import json
#2A
def zipcode_info(countrycode, zipcode):
    url = f"https://api.zippopotam.us/{countrycode}/{zipcode}"
    with urllib.request.urlopen(url) as request:
        response = request.read().decode()

    return response

#2B
class Place:
    def __init__(self, data):
        self.name = data["place name"]
        self.longitude = data["longitude"]
        self.latitude = data["latitude"]
        self.state = data["state"]

def zipcode_info(countrycode, zipcode):
    url = f"https://api.zippopotam.us/{countrycode}/{zipcode}"
    with urllib.request.urlopen(url) as request:
        response = request.read().decode()

    data = json.loads(response)
    return [Place(place) for place in data["places"]]



#test code
print(zipcode_info("US", "02861"))

places = zipcode_info("US", "02861")
for place in places:
        print(f"Place: {place.name}, State: {place.state}, Latitude: {place.latitude}, Longitude: {place.longitude}")