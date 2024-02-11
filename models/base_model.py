#!/usr/bin/python3

import uuid
from datetime import datetime
from __init__ import storage


"""
a class BaseModel that defines all common attributes/methods for other classes
"""
class BaseModel:
    """
    A class tha 

    Attrirbutes:

    Methods:

    """
    def __init__(self, *args, **kwargs):
        """
        Constructs a new instance of the squere class.

        parameters:
        size (int): the size of a side of the square
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dt%H:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """Update the instance of object with current date and time
        """
        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        """Return a string representation of BaseModel
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def to_dict(self):
        """Return the dictionary of object that contains keys and value
        """
        obj = self.__dict__.copy()
        obj["__class__"] = self.__class__.__name__
        obj["update_at"] = self.updated_at.isoformat()
        obj["creat_at"] = self.created_at.isoformat()
        return obj
