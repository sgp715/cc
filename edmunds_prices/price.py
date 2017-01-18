import json
import requests

# sample endpoint call to get Model Year ID/Style ID:
# http://api.edmunds.com/api/vehicle/v2/honda/civic/1992?fmt=json&api_key=kaqxy8y935hwyk8r5scjs34w

def get_car_json(make, model, year):

    with open('./creds.json') as f:
        key = json.load(f)['api_key']

    base_url = 'http://api.edmunds.com'
    version = 'api/vehicle/v2'
    fmt = '?fmt=json'
    state = '&state=used'
    key = '&api_key=' + key


    endpoint = '/'.join((base_url, version, make, model, str(year)))
    endpoint += (fmt + state + key)

    response = requests.get(endpoint)

    if response.status_code != 200:
        return None

    return response.json()

def parse_style_id(car_json):

    pass

def get_prices():

    pass

def good_deal():

    pass
