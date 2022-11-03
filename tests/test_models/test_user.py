#!/usr/bin/python3
"""
Module test user
"""


import unittest
import os
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Clas TestUser testing to the class User
    creating a new user"""
    def setUp(clas):
        clas.new_user = User()
        clas.new_user.first_name = "Juan"
        clas.new_user.last_name = "Hernandez"
        clas.new_user.email = "new_class@holbertonstudents.com"
        clas.new_user.password = "new_class123"

    def test_subclass(self):
        self.assertTrue(issubclass(self.new_user.__class__, BaseModel), True)

    def test_is_None(self):
        self.assertIsNotNone(User.__doc__)

    def test_attributes(self):
        self.assertTrue('email' in self.new_user.__dict__)
        self.assertTrue('id' in self.new_user.__dict__)
        self.assertTrue('created_at' in self.new_user.__dict__)
        self.assertTrue('updated_at' in self.new_user.__dict__)
        self.assertTrue('password' in self.new_user.__dict__)
        self.assertTrue('first_name' in self.new_user.__dict__)
        self.assertTrue('last_name' in self.new_user.__dict__)

    def test_strings(self):
        self.assertEqual(type(self.new_user.email), str)
        self.assertEqual(type(self.new_user.password), str)
        self.assertEqual(type(self.new_user.first_name), str)
        self.assertEqual(type(self.new_user.last_name), str)

    def test_save(self):
        self.new_user.save()
        self.assertNotEqual(self.new_user.created_at, self.new_user.updated_at)

    def test_to_dict_method(self):
        self.assertEqual('to_dict' in dir(self.new_user), True)

if __name__ == '__main__':
    unittest.main()