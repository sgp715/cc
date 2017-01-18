import logging

import re
from datetime import datetime
from craigslist import CraigslistForSale

def parse_name(car):
    """
    given a car dict, find data seperate out the make, model and year
    into new fields
    """
    now = datetime.now()
    year_short = str(now.year)[2:]

    words = re.split(' ', car)

    year_index = None
    year = None
    for (i, word) in enumerate(words):
        word_length = len(word)
        if word_length == 2:
            if (re.match('[0-9]{2}', word)) != None:
                years_to_add = 1900
                if (int(word) <= int(year_short)):
                    years_to_add = 2000
                year = int(word) + years_to_add
                year_index = i
                break
        if word_length == 4:
            if (re.match('[1-3][0-9]{3}', word)) != None:
                year = int(word)
                year_index = i
                break

    car_dict = {'success': [], 'shite': []}

    # TODO: logging
    if (year_index == None):
        car_dict['shite'].append(car)

    try:
        make = words[year_index + 1].lower()
        model = words[year_index + 2].lower()
        car_dict['success'].append(car)

    except:
        car_dict['shite'].append(car)

    return car_dict

def get_generator(site, max_price):

    clist = CraigslistForSale(site=site,
                              category='cto',
                              filters={'max_price': max_price})

    return clist.get_results(sort_by='newest')

def create_datetime(datetime_array):

    re_groups = re.match('([0-9]{4})-([0-9]{1,2})-([0-9]{1,2}) ([0-9]{1,2}):([0-9]{1,2})', datetime_array).groups()
    year = int(re_groups[0])
    month = int(re_groups[1])
    day = int(re_groups[2])
    hour = int(re_groups[3])
    minute = int(re_groups[4])
    car_datetime = datetime(year, month, day, hour, minute)

    return car_datetime

def find_new_cars(generator, most_recent):
    """
    takes the site (e.g. Seattle), max_price, and most_recent previosly checked car
    and it returns all after the most_recent
    """

    new_cars = []

    for car in generator:

        car_datetime = create_datetime(car['datetime'])
        most_recent_datetime = create_datetime(most_recent['datetime'])

        # might skip some here
        if car_datetime < most_recent_datetime:
            break

        if car_datetime == most_recent_datetime:
            if car == most_recent:
                continue
            break

        new_cars.append(car)

    return new_cars
