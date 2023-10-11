#!/usr/bin/env python3

""" This model defines all common attributes/method for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    class that defines all common attributes
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
    
    def save(self):
        """
        updates public instance attribute updated_at
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys and values
        """
        new_dict = {}
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                new_dict[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if not value:
                    pass
                else:
                    new_dict[key] = value
        new_dict['__class__'] = self.__class__.__name__
        return new_dict

    def __str__(self):
        """
        Returns the string representation of the dict id
        """
        class_name = self.__class__.__name__
        my_dict = {k: v for (k, v) in self.__dict__.items() if (not v) is False}
        return "[" + class_name + "]" + "(" + self.id + ")" + str(my_dict)
