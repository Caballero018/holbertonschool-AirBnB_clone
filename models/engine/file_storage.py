#!/usr/bin/python3
"""

"""

import os
import json
import datetime


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        k = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[k] = obj

    def save(self):
         with open(FileStorage.__file_path, "w+") as f:
            d = {k: str(v) for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            FileStorage.__objects = json.load(f)
