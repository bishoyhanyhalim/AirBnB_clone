#!/usr/bin/python3
"""Base_model test module."""
from models.base_model import BaseModel
from unittest import TestCase
import unittest
import os
import json
import uuid
import datetime


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

    def test_save(self):
        """Save testing."""
        new = BaseModel()
        new.save()
        key = f"{new.__class__.__name__}.{new.id}"
        with open('file.json', 'r') as fl:
            load = json.load(fl)
            self.assertEqual(load[key], new.to_dict())

    def test_str(self):
        """Str method test."""
        new = BaseModel()
        self.assertEqual(str(new), '[{}] ({}) {}'.
                         format(new.__class__.__name__, new.id, new.__dict__))

    def test_to_dict(self):
        """To_dict test."""
        obj = BaseModel()
        dicti = obj.to_dict()
        self.assertEqual(obj.to_dict(), dicti)

    def test_created_at(self):
        """Created at test."""
        new = BaseModel()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """Test updated at"""
        new = BaseModel()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        new2 = new.to_dict()
        new = BaseModel(**new2)
        self.assertFalse(new.created_at == new.updated_at)

    def test_kwargs_one(self):
        """Kwargs test."""
        dicti = {'id': 123}
        with self.assertRaises(KeyError):
            new5 = BaseModel(**dicti)


if __name__ == '__main__':
    unittest.main()
