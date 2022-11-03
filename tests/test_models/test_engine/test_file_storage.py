#!/usr/bin/python3
"""
"""
import unittest
import os
import json
import datetime

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Sets up the class test"""

        self.b1 = BaseModel()
        self.a1 = Amenity()
        self.c1 = City()
        self.p1 = Place()
        self.r1 = Review()
        self.s1 = State()
        self.u1 = User()
        self.storage = FileStorage()
        self.storage.save()
        if os.path.exists("file.json"):
            pass
        else:
            os.mknod("file.json")

    def tearDown(self):
        """Tears down the testing environment"""

        del self.b1
        del self.a1
        del self.c1
        del self.p1
        del self.r1
        del self.s1
        del self.u1
        del self.storage
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """Check the all"""
        obj = self.storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, self.storage._FileStorage__objects)

    def test__file_path(self):
        fp = FileStorage()
        self.assertTrue(FileStorage._FileStorage__file_path)

    def test_storage_empty(self):
        """check the storage is not empty"""
        self.assertIsNotNone(self.storage.all())

    def test_storage_all_type(self):
        """check the type of storage"""

        self.assertEqual(dict, type(self.storage.all()))

    def test_new(self):
        """check the new user"""
        obj = self.storage.all()
        self.u1.id = 1234
        self.u1.name = "Juan"
        self.storage.new(self.u1)
        key = "{}.{}".format(self.u1.__class__.__name__, self.u1.id)
        self.assertIsNotNone(obj[key])

    def test_check_json_loading(self):
        """ Checks if methods from Storage Engine works."""

        with open("file.json") as f:
            dic = json.load(f)

            self.assertEqual(isinstance(dic, dict), True)

    def test_reload(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        storage.new(bm)
        storage.new(us)
        storage.new(st)
        storage.new(pl)
        storage.new(cy)
        storage.new(am)
        storage.new(rv)
        storage.save()
        storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
        self.assertIn("User." + us.id, objs)
        self.assertIn("State." + st.id, objs)
        self.assertIn("Place." + pl.id, objs)
        self.assertIn("City." + cy.id, objs)
        self.assertIn("Amenity." + am.id, objs)
        self.assertIn("Review." + rv.id, objs)

        def test_reload_no_file(self):
        self.assertRaises(FileNotFoundError, storage.reload())

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            storage.reload(None)

    """def test_save(self):
        bas2 = storage.all()
        for k in bas2.keys():
            obj = bas2[k]
        bas1 = BaseModel()
        val = datetime.datetime(2017, 9, 28, 21, 7, 25, 47381)
        setattr(bas1, "updated_at", val.isoformat())
        bas1.save()
        storage.reload()
        self.assertNotEqual(bas1, obj)"""

    def test_file_existence(self):
        """
        Checks if methods from Storage Engine works.
        """
        with open("file.json") as f:
            self.assertTrue(len(f.read()) > 0)

    def test_docstrings(self):
        """Check the docString each function"""
        self.assertTrue(FileStorage.all.__doc__)
        self.assertTrue(hasattr(FileStorage, 'all'))
        self.assertTrue(FileStorage.new.__doc__)
        self.assertTrue(hasattr(FileStorage, 'new'))
        self.assertTrue(FileStorage.save.__doc__)
        self.assertTrue(hasattr(FileStorage, 'save'))
        self.assertTrue(FileStorage.reload.__doc__)
        self.assertTrue(hasattr(FileStorage, 'reload'))

if __name__ == '__main__':
    unittest.main()