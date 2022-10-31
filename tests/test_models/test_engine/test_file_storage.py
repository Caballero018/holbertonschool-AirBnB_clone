#!/usr/bin/python3
"""

"""
import unittest
import os
import json
import models

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestFileStorage(unittest.TestCase):
    def test__file_path(self):
        self.storage = FileStorage()
        self.storage.save()
        if os.path.exists("file.json"):
            pass
        else:
            os.mknod("file.json")