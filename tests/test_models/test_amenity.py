#!/usr/bin/python3
"""
Module test amenity
"""


import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Clas TestState testing to the class User
    creating a new user"""
    def setUp(clas):
        clas.amenity1 = Amenity()
        clas.amenity1.name = "Gym"

    @classmethod
    def tearDownClass(clas):
        del clas.amenity1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_subclass(self):
        self.assertTrue(isssubclass(self.amenity1.__class__, BaseModel), True)

    def test_is_None(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes(self):
        self.assertTrue('name' in self.amenity1.__dict__)

    def test_strings(self):
        self.assertEqual(type(self.amenity1.name), str)

    def test_save(self):
        self.amenity1.save()
        self.assertNotEqual(self.amenity1.created_at, self.amenity1.updated_at)

    def test_to_dict_method(self):
        self.assertEqual('to_dict' in dir(self.amenity1), True)

if __name__ == '__main__':
    unittest.main()