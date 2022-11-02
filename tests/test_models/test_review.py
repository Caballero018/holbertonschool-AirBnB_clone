#!/usr/bin/python3
"""
Module test user
"""


import unittest
import os
from models.riview import Riview
from models.base_model import BaseModel


class TestRiview(unittest.TestCase):
    def setUpClass(cls):
        cls.review1 = Riview()
        cls.review1.place_id = "Florida/Orlando-Sant Lois Hotel"
        cls.review1.user_id = "Alejandro"
        cls.review1.text = "First Class"

    @classmethod
    def tearDownClass(cls):
        del cls.review1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.review1.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        self.assertIsNotNone(Review.__doc__)

    def test_has_attributes(self):
        self.assertTrue('id' in self.review1.__dict__)
        self.assertTrue('created_at' in self.review1.__dict__)
        self.assertTrue('updated_at' in self.review1.__dict__)
        self.assertTrue('place_id' in self.review1.__dict__)
        self.assertTrue('user_id' in self.review1.__dict__)
        self.assertTrue('text' in self.review1.__dict__)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.review1.text), str)
        self.assertEqual(type(self.review1.user_id), str)
        self.assertEqual(type(self.review1.place_id), str)

    def test_save(self):
        self.place1.save()
        self.assertNotEqual(self.review1.created_at, self.review1.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.review1), True)

if __name__ == '__main__':
    unittest.main()