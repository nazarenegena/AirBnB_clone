#!/usr/bin/python3
"""This is a module for  class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class is for defining a user"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
