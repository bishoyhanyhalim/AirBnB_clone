#!/usr/bin/python3
"""city test case module"""
import unittest
import os
import models
from models.city import City


class TestCity(unittest.TestCase):

    def setUp(self):
        """the set tests method"""
        self.city = City()

    def test_the_attribute(self):
        """the attribute values tests method"""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")


if __name__ == '__main__':
    unittest.main()
