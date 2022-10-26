#!/usr/bin/python3
"""
Module file_storage that add the dicts
"""


import os
import json
import datetime


class FileStorage:
    """Class FileStorage that save dictionaries in JSON"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the objects"""
        return FileStorage.__objects

    def new(self, obj):
        """creates a new object in JSON file
        obj: is the base object"""
        k = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[k] = obj

    def save(self):
        """Save the dict in JSON file"""
        with open(FileStorage.__file_path, "w+") as f:
            d = {k: str(v) for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """reloads and updates the previos dictionary"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            FileStorage.__objects = json.load(f)
