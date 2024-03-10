#!/usr/bin/python3
"""Base_model test module."""
from models.base_model import BaseModel
from unittest import TestCase
import unittest
import os
import json
import uuid


class test_basemodel(TestCase):
    """Test class of basemodel."""

    def setUp(self):
        """Set up for every test."""
        pass

    def tearDown(self):
        """Tear down after each test."""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_default(self):
        """Creating an instance with default values."""
        instance = BaseModel()
        self.assertEqual(type(instance), BaseModel)

    def test_kwargs(self):
        """Tests creating a new instance using to_dict."""
        instance = BaseModel()
        inst_dict = instance.to_dict()
        new = BaseModel(**inst_dict)
        self.assertFalse(new is instance)

    def test_kwargs_int(self):
        """Creating instance using invalid input."""
        instance = BaseModel()
        inst_dict = instance.to_dict()
        inst_dict.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**inst_dict)

    def test_kwargs_none(self):
        """Creating an instance with none kwargs."""
        t_dict = {None, None}
        with self.assertRaises(TypeError):
            new = BaseModel(**t_dict)

    def test_id(self):
        """Test id attribute."""
        new = BaseModel()
        self.assertEqual(type(new.id), str)


if __name__ == '__main__':
    unittest.main()
