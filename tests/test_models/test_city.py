#!/usr/bin/python3
"""
Module test state
"""


import unittest
import os
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Clas TestState testing to the class User
    creating a new user"""
    def setUp(clas):
        clas.city1 = City()
        clas.city1.state_id = "Florida"
        clas.city1.name = "Florida"

    @classmethod
    def tearDownClass(clas):
        del clas.city1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_subclass(self):
        self.assertTrue(isssubclass(self.city1.__class__, BaseModel), True)

    def test_is_None(self):
        self.assertIsNotNone(City.__doc__)

    def test_attributes(self):
        self.assertTrue('name' in self.city1.__dict__)
        self.assertTrue('state_id' in self.city1.__dict__)

    def test_strings(self):
        self.assertEqual(type(self.city1.name), str)
        slef.assertEqual(type(self.city1.state_id), str)

    def test_save(self):
        self.city1.save()
        self.assertNotEqual(self.city1.created_at, self.city1.updated_at)

    def test_to_dict_method(self):
        self.assertEqual('to_dict' in dir(self.city1), True)

if __name__ == '__main__':
    unittest.main()