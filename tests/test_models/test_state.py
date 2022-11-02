#!/usr/bin/python3
"""
Module test state
"""


import unittest
import os
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Clas TestState testing to the class User
    creating a new user"""
    def setUp(clas):
        clas.state1 = State()
        clas.state1.name = "Florida_State_Sant_Lois_Hotel"

    @classmethod
    def tearDownClass(clas):
        del clas.state1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_subclass(self):
        self.assertTrue(isssubclass(self.state1.__class__, BaseModel), True)

    def test_is_None(self):
        self.assertIsNotNone(State.__doc__)

    def test_attributes(self):
        self.assertTrue('name' in self.state1.__dict__)
        self.assertTrue('id' in self.state1.__dict__)
        self.assertTrue('created_at' in self.state1.__dict__)
        self.assertTrue('updated_at' in self.state1.__dict__)

    def test_strings(self):
        self.assertEqual(type(self.state1.name), str)

    def test_save(self):
        self.state1.save()
        self.assertNotEqual(self.state1.created_at, self.state1.updated_at)

    def test_to_dict_method(self):
        self.assertEqual('to_dict' in dir(self.state1), True)

if __name__ == '__main__':
    unittest.main()