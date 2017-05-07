import json
import requests

api_key = 'AIzaSyCJ9wJjgzrnrtOnZ0Cbl3Wjzwy5szKv4Zg'
base_url = 'https://maps.googleapis.com/maps/api/geocode/json'


def prepare_address(address):
    """Convert address string into url friendly string."""
    url_address = address.split(' ')
    url_address = "+".join(url_address)
    print(url_address)
    return url_address


def create_url(address):
    """Create url for api call."""
    url = base_url
    param_1 = 'address=' + prepare_address(address)
    param_2 = 'key=' + api_key
    geocode_url = '{url}?{param_1}&{param_2}'.format(url=url,
                                                     param_1=param_1,
                                                     param_2=param_2)
    print(geocode_url)
    return geocode_url


def geocode(address):
    """Return geocode information from google maps api."""
    request_url = create_url(address)
    print request_url
    json_data = requests.get(request_url)
    data = json.loads(json_data.text)
    location = data["results"][0]["geometry"]["location"]
    council = data["results"][0]["address_components"][3]["short_name"]
    results = {"lat": location["lat"],
               "lng": location["lng"],
               "council": council
               }
    print results
    return results


# test
geocode("85 ALBION STREET, ANNANDALE NSW 2038")
