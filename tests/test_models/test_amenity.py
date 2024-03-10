#!/usr/bin/python3
"""amenity test case module"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def setUp(self):
        """the set tests method"""
        self.amenity = Amenity()

    def test_the_attribute(self):
        """the attribute values tests method"""
        self.assertEqual(self.amenity.name, "")

    def test_this_attribute(self):
        """the assigning attribute of amenity tests method"""
        with self.assertRaises(AttributeError):
            self.amenity.undefined_attribute = "don't work this"


if __name__ == '__main__':
    unittest.main()
