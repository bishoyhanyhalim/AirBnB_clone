#!/usr/bin/python3
"""this is a user class"""

from models.base_model import BaseModel


class User(BaseModel):
    """this is a user class , with empty strings"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
