#!/usr/bin/python3
"""state test case module"""
import unittest
from models.state import State


class TestState(unittest.TestCase):

    def setUp(self):
        """the set tests method"""
        self.state = State()

    def test_the_attribute(self):
        """the attribute values tests method"""
        self.assertEqual(self.state.name, "")
        self.assertEqual(self.state.id, "")

    def test_this_attribute(self):
        """the assigning attribute of state tests method"""
        with self.assertRaises(AttributeError):
            self.state.undefined_attribute = "don't work this"


if __name__ == '__main__':
    unittest.main()
