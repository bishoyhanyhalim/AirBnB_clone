#!/usr/bin/python3
"""place test case module"""
import unittest
import os
import models
from models.place import Place


class TestPlace(unittest.TestCase):

    def setUp(self):
        """the set tests method"""
        self.place = Place()

    def test_the_attribute(self):
        """the attribute values tests method"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")


if __name__ == '__main__':
    unittest.main()
