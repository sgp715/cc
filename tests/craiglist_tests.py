# import sys
# from os import path
# sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

import unittest
from datetime import datetime
from craigslist_cars import cars


class TestCraigsList(unittest.TestCase):

    unittest.sample_data = [{'name': u'1995 Saturn SL1', 'has_image': False, 'url': u'http://seattle.craigslist.org/sno/cto/5915267154.html', 'has_map': True, 'price': u'$350', 'geotag': None, 'where': u'baring', 'id': u'5915267154', 'datetime': u'2016-12-11 13:33'},
                            {'name': u'89 honda civic', 'has_image': False, 'url': u'http://seattle.craigslist.org/skc/cto/5885318054.html', 'has_map': True, 'price': u'$750', 'geotag': None, 'where': u'Renton', 'id': u'5885318054', 'datetime': u'2016-12-11 13:30'},
                            {'name': u'Mechanics Special 2002 Ford Focus', 'has_image': True, 'url': u'http://seattle.craigslist.org/tac/cto/5915262376.html', 'has_map': True, 'price': u'$500', 'geotag': None, 'where': u'Puyallup', 'id': u'5915262376', 'datetime': u'2016-12-11 13:29'},
                            {'name': u'superduty f250 f350 truck bed canopy', 'has_image': True, 'url': u'http://seattle.craigslist.org/sno/cto/5913752396.html', 'has_map': True, 'price': u'$350', 'geotag': None, 'where': u'lynnwood', 'id': u'5913752396', 'datetime': u'2016-12-11 13:32'},
                            {'name': u'ex 98 Honda Civic', 'has_image': True, 'url': u'http://seattle.craigslist.org/see/cto/5899106811.html', 'has_map': True, 'price': u'$1000', 'geotag': None, 'where': u'Renton', 'id': u'5899106811', 'datetime': u'2016-12-11 13:27'},
                            {'name': u'2004 Saab 9-3 Aero - Mechanic Special', 'has_image': True, 'url': u'http://seattle.craigslist.org/skc/cto/5901617901.html', 'has_map': True, 'price': u'$950', 'geotag': None, 'where': u'Burien', 'id': u'5901617901', 'datetime': u'2016-12-11 13:27'}]

    def test_parse_name(self):

        name0 = unittest.sample_data[0]['name']
        expected = (1995, 'saturn', 'sl1')
        actual = cars.parse_name(name0)
        self.assertEqual(expected, actual)

        name1 = unittest.sample_data[1]['name']
        expected = (1989, 'honda', 'civic')
        actual = cars.parse_name(name1)
        self.assertEqual(expected, actual)

        name2 = unittest.sample_data[2]['name']
        expected = (2002, 'ford', 'focus')
        actual = cars.parse_name(name2)
        self.assertEqual(expected, actual)

        name3 = unittest.sample_data[3]['name']
        expected = None
        actual = cars.parse_name(name3)
        self.assertEqual(expected, actual)

    def test_create_datetime(self):

        datetime_array = unittest.sample_data[2]['datetime']
        larger = datetime(2016, 12, 11, 13, 30)
        smaller = cars.create_datetime(datetime_array)
        if larger > smaller:
            self.assertEqual(1, 1)
        else:
            self.assertEqual(0, 1)

    def test_find_new_cars(self):

        most_recent = unittest.sample_data[2]

        expected = [{'name': u'1995 Saturn SL1', 'has_image': False, 'url': u'http://seattle.craigslist.org/sno/cto/5915267154.html', 'has_map': True, 'price': u'$350', 'geotag': None, 'where': u'baring', 'id': u'5915267154', 'datetime': u'2016-12-11 13:33'},
                    {'name': u'89 honda civic', 'has_image': False, 'url': u'http://seattle.craigslist.org/skc/cto/5885318054.html', 'has_map': True, 'price': u'$750', 'geotag': None, 'where': u'Renton', 'id': u'5885318054', 'datetime': u'2016-12-11 13:30'}]
        actual = cars.find_new_cars(unittest.sample_data ,most_recent)
        self.assertListEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
