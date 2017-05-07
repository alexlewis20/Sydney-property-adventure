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


create_url("85 ALBION STREET, ANNANDALE NSW 2038")
