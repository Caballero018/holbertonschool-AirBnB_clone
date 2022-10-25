#!/usr/bin/python3
"""
Module Base
get id and time changes
"""

'''Imports'''
import uuid
from datetime import datetime


class BaseModel:
    '''Base class to string and datas'''
    def __init__(self):
        '''initialization of datas od dictionary's'''
        self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()

    
    def __str__(self):
        '''str'''
        return ("[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        '''save method to updates the attribute updated_at'''
        self.updated_at = datetime.now()
    
    def to_dict(self):
        '''JSON to dictionary'''
        my_dictionary = self.__dict__.copy()
        my_dictionary['__class__'] = type(self).__name__
        my_dictionary["created_at"] = my_dictionary["created_at"].isoformat()
        my_dictionary["updated_at"] = my_dictionary["updated_at"].isoformat()
        return my_dictionary