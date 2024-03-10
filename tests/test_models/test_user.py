#!/usr/bin/python3
"""user test case module"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        """the set tests method"""
        self.user = User()

    def test_str_attribute_value(self):
        """the non-string of user tests method"""
        with self.assertRaises(TypeError):
            self.user.email = 707

    def test_input_of_attributes(self):
        """the setting tests method"""
        self.user.email = "bishoy@gmail.com"
        self.user.password = "thisIsPass"
        self.user.first_name = "bishoy"
        self.user.last_name = "hany"

        self.assertEqual(self.user.email, "bishoy@gmail.com")
        self.assertEqual(self.user.first_name, "bishoy")
        self.assertEqual(self.user.password, "thisIsPass")
        self.assertEqual(self.user.last_name, "hany")

    def test_this_attribute(self):
        """the assigning attribute of user tests method"""
        with self.assertRaises(AttributeError):
            self.user.undefined_attribute = "don't work this"

    def test_does_this_dict(self):
        """the dictionary of user tests method"""
        user_dict = self.user.to_dict()
        self.assertIn('email', user_dict)
        self.assertIn('last_name', user_dict)
        self.assertIn('first_name', user_dict)
        self.assertIn('password', user_dict)

    def test_the_dict(self):
        """the initializing dictionary of user tests method"""
        info_data = {
            'email': 'bishoy@gmail.com',
            'password': 'thisIsPass',
            'first_name': 'bishoy',
            'last_name': 'hany',
        }

        new_user = User(**info_data)

        self.assertEqual(new_user.email, "bishoy@gmail.com")
        self.assertEqual(new_user.first_name, "bishoy")
        self.assertEqual(new_user.password, "thisIsPass")
        self.assertEqual(new_user.last_name, "hany")

    def test_the_attribute(self):
        """the attribute values tests method"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")


if __name__ == '__main__':
    unittest.main()
