#!/usr/bin/python3
"""the review class module"""

from models.base_model import BaseModel


class Review(BaseModel):
    # inherits from basemodel
    place_id = ""
    user_id = ""
    text = ""
