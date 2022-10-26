#!/usr/bin/python3
"""
Module file_storage that add the dicts
"""


import os
import json 


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
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """reloads and updates the previos dictionary"""
        from models.base_model import BaseModel
        if not os.path.isfile(FileStorage.__file_path):
            return
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                loaded_dict = json.load(f)

                for key, value in loaded_dict.items():
                    obj = eval(value["__class__"])(**value)
                    FileStorage.__objects[key] = obj
        except Exception as e:
            pass
