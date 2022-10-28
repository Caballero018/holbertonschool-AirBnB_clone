#!/usr/bin/python3
"""
Module Class User
creates the structure of data of a user
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Attributes of class of a user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
