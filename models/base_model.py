#!/usr/bin/python3
"""
Module Base
get id and time changes
"""


import uuid
from datetime import datetime


class BaseModel:
    '''Base class to string and datas'''
    def __init__(self, *args, **kwargs):
        '''initialization of datas od dictionary's'''
        self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()

    def __str__(self):
        '''str'''
        return ("[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__
                ))

    def save(self):
        '''save method to updates the attribute updated_at'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''JSON to dictionary'''
        dictionary = self.__dict__.copy()
        for k in dictionary.keys():
            if k == "updated_at":
                dictionary[k] = dictionary[k].isoformat()
            if k == "created_at":
                dictionary[k] = dictionary[k].isoformat()
        return dictionary
