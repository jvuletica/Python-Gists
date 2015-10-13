#! /usr/bin/env python3
import unittest, within100km, math

class CustomerLocationAndDistanceTests(unittest.TestCase):
    def setUp(self):
        self.test_instance = third.CustomersWithinDistance()
    def test_constants(self):
        self.assertEqual(self.test_instance.OFFICE_LAT, math.radians(53.3381985))
        self.assertEqual(self.test_instance.OFFICE_LONG, math.radians(-6.2592576))
        self.assertEqual(self.test_instance.EARTH_RADIUS, 6371)
    def test_jsonToDict(self):
        assert type(self.test_instance.oneLineOfJsonToDict('{"name": "josip"}')) \
            is dict
    def test_distanceCalculation(self):
        self.assertEqual(self.test_instance
        .calculateDistanceFromOffice(53.3381985, -6.2592576), 0)
    def test_sort(self):
        sorted_list = self.test_instance.sortCustomersWithinDistanceList()
        for index, customer in enumerate(sorted_list):
            self.assertLess(customer["user_id"], sorted_list[index + 1]["user_id"])
if __name__ == "__main__":
    unittest.main()
