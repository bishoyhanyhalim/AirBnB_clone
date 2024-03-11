#!/usr/bin/python3
"""amenity test case module"""
import unittest
import os
import models
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def setUp(self):
        """the set tests method"""
        self.amenity = Amenity()

    def test_the_attribute(self):
        """the attribute values tests method"""
        self.assertEqual(self.amenity.name, "")


if __name__ == '__main__':
    unittest.main()
