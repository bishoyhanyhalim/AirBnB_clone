#!/usr/bin/python3
"""review test case module"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):

    def setUp(self):
        """the set tests method"""
        self.review = Review()

    def test_the_attribute(self):
        """the attribute values tests method"""
        self.assertEqual(self.review.text, "")
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")

    def test_this_attribute(self):
        """the assigning attribute of review tests method"""
        with self.assertRaises(AttributeError):
            self.review.undefined_attribute = "don't work this"


if __name__ == '__main__':
    unittest.main()
