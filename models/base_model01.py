#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    """This class defines the common attributes and methods for other classes"""
    
    def __init__(self):
        """Initializes a BaseModel instance with a unique id, created_at and updated_at attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance in the format:
        [<class name>] (<self.id>) <self.__dict__>"""
        return '[{}] ({}) {}'.format(
            self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """Updates the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """Returns a dictionary representation of the instance, with added class name and converted created_at and updated_at to ISO format strings"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
