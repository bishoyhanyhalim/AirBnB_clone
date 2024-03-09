#!/usr/bin/python3
"""this is a Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class for project"""

    place_id = ""
    user_id = ""
    text = ""
