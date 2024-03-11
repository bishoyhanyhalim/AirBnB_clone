#!/usr/bin/python3
"""BaseModel class module."""
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel class."""
    def __init__(self, *args, **kwargs):
        """BaseModel initialization."""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'id':
                        if not isinstance(value, str):
                            raise KeyError
                    if key in ['updated_at', 'created_at']:
                        setattr(self, key, datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """BaseModel string representation."""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Save to json file."""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert to dict."""
        ins_dict = self.__dict__.copy()
        ins_dict['__class__'] = self.__class__.__name__
        ins_dict['created_at'] = self.created_at.isoformat()
        ins_dict['updated_at'] = self.updated_at.isoformat()
        return ins_dict
