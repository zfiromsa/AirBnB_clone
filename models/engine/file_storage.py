#!/usr/bin/python3

import json 
from os import path

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return  the dictionary of all obects."""
        return self.__objects
    
    def new(self, obj):
        """creat new object"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serialize """
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)
    
    def reload(self):
        """deserialize """
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                from models.base_model import BaseModel
                from models.amenity import Amenity
                from models.user import User
                from models.city import City
                from models.place import Place
                from models.state import State
                from models.review import Review
                for key, value in data.items():
                    Cl_name, obj_id = key.split('.')
                    if Cl_name in key:
                        instance = BaseModel(**value)
                    if Cl_name in key:
                        instance = User(**value)
                    elif Cl_name in key:
                        instance = Place(**value)
                    elif Cl_name in key:
                        instance = State(**value)
                    elif Cl_name in key:
                        instance = Review(**value)
                    elif Cl_name in key:
                        instance = City(**value)
                    elif Cl_name in key:
                        instance = Amenity(**value)
                    else:
                        continue
                    self.__objects[key] = instance
        except FileNotFoundError:
            pass
        except json.JSONDecodeError as e:
            print(e)
                    
