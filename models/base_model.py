import uuid
from datetime import datetime

class BaseModel:
    """
    A base class that defines common attributes and methods for other classes.

    Public instance attributes:
        id (str): Assigned with a UUID when an instance is created.
                  It provides a unique identifier for each BaseModel instance.
        created_at (datetime): Assigned with the current datetime when an instance is created.
        updated_at (datetime): Assigned with the current datetime when an instance is created,
                               and it will be updated every time the object is modified.

    Public instance methods:
        save(): Updates the public instance attribute updated_at with the current datetime.
        to_dict(): Returns a dictionary containing all keys and values of the instance's __dict__.
                   Only instance attributes set will be included.
                   The dictionary representation includes the '__class__' key with the class name.
                   'created_at' and 'updated_at' are converted to string objects in ISO format.

    """
    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.
        Assigns a unique id using UUID, sets the created_at and updated_at attributes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.

        Returns:
            dict: A dictionary containing all keys and values of the instance's __dict__.
                  Includes the '__class__' key with the class name.
                  'created_at' and 'updated_at' attributes are converted to string objects in ISO format.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
