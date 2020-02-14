#!/usr/bin/python3

from datetime import datetime
from models.__init__ import storage
import uuid

"""
    Class base for the others classes
"""


class BaseModel():

    def __init__(self, *args, **kwargs):
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
            for key, value in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, value)

    def __str__(self):
        """ bla bla bla """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        ans = self.__dict__
        ans.update({'__class__': __class__.__name__})
        ans['created_at'] = ans['created_at'].isoformat()
        ans['updated_at'] = ans['updated_at'].isoformat()
        return ans
