#!/usr/bin/python3
"""
Module review of the place
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """class Review with attr of id information"""
    place_id = ""
    user_id = ""
    text = ""
