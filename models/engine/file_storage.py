#!/usr/bin/python3
# the file storage class
# serialization & deserialization of obj instances
# class that serializes instances to a JSON file &
# deserializes JSON file back to instances

import datetime
import json
import os

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


"""FileStorage class module."""


class FileStorage():
    """
       serializes instances to a JSON file and
       deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    # public instance methods

    def all(self):
        """
        Returns the dictionary __objects
        """
        __objects = self.__dict__
        return __objects

    def new(self, obj):
        """ the __objects key is created & assigned to obj_key
          combine the classname with the objects id
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    # serialize the object instance as a file
    def save(self):
        """
        Serialize __objects to the JSON file
        """
        with open(self.__file_path, mode="w") as f:
            dict_storage = {}
            for key, value in self.__objects.items():
                dict_storage[key] = value.to_dict()
            json.dump(dict_storage, f)

    # method to deserialize json file to obj
    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except FileNotFoundError:
            pass
