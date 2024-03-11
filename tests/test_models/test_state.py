#!/usr/bin/python3
"""state test case module"""
import unittest
import os
import models
from models.state import State


class TestState(unittest.TestCase):

    def setUp(self):
        """the set tests method"""
        self.state = State()

    def test_the_attribute(self):
        """the attribute values tests method"""
        self.assertEqual(self.state.name, "")


if __name__ == '__main__':
    unittest.main()
