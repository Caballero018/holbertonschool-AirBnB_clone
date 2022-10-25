#!/usr/bin/python3
"""

"""

'''Imports'''
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def __str__(self):
        return ("[{}] ({}) ({})".format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()
    
    def to_dict(self):
        my_dictionary = self.__dict__.copy()
        my_dictionary['__class__'] = type(self).__name__
        my_dictionary["created_at"] = my_dictionary["created_at"].isoformat()
        my_dictionary["updated_at"] = my_dictionary["updated_at"].isoformat()
        return my_dictionary