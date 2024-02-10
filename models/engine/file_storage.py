#!/usr/bin/python3

import json 
from os import path
from models.user import User

class FileStrorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return  the dictionary of all obects."""
        return self.__objects
    
    def new(self, obj):
        """ """
        key = "{}.{}.format(obj.__class__.__name__, obj.id)"
        self.__objects[key] = obj

    def save(self):
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'W') as file:
            json.dump(serialized_objects, file)
    
    def reload(self):
        """ """
        if path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                try:
                    data = json.load(file)
                    for key, obj_dict in data.items():
                        class_name, obj_id = key.split('.')
                        if class_name == "User":
                            obj = User(**obj_dict)
                        else:
                            module = __import__("moduls." + class_name, fromlist=[class_name])
                            cls = getattr(module, class_name)
                            obj = cls(**obj_dict)
                        self.__objects[key] = obj
                except json.JSONDecodeError:
                    pass
                    
