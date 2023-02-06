#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    """A base class for all models in our hbnb clone.

    Public instance attributes:
        id: string - assign with an uuid when an instance is created.
        created_at: datetime - assign with the current datetime when an instance is created.
        updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
    """

    def __init__(self, *args, **kwargs):
        """Instantiates a new model.

        Args:
            *args: a variable length argument list.
            **kwargs: a variable length keyword argument list.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
        if kwargs:
            self.__dict__.update(kwargs)
            if 'created_at' in kwargs.keys():
                self.created_at = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs.keys():
                self.updated_at = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
    
    def __str__(self):
        """Returns a string representation of the insta"""
        cls = str(type(self)).split('.')[-1].split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates the `updated_at` attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the instance.

        The dictionary contains all keys and values of the instance __dict__,
        with the following additional keys:
            __class__: the class name of the object.
            created_at: the `created_at` attribute in ISO format.
            updated_at: the `updated_at` attribute in ISO format.
        """
        members = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary['__class__'] = str(type(self)).split('.')[-1].split('\'')[0]
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated
