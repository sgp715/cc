from craigslist import CraigslistForSale
import json
import time
from craigslist_cars import cars


with open('./config.json') as f:
    config = json.load(f)

def flag_cars(success, shite):

    first = True
    for new in success:

        if first:
            most_recent = new
            first = True

        # try to get the price
        # if it doesn't work stick it on shite

# gen = cars.get_generator(config['site'], config['max_price'])
# new_cars = cars.find_new_cars(gen, most_recent)
