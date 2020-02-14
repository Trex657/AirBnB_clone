#!/usr/bin/python3

from datetime import datetime
import models
import uuid

"""
    Class base for the others classes
"""


class BaseModel():

    def __init__(self, *args, **kwargs):
        if (len(kwargs) > 0):
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self.to_dict())

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        ans = self.__dict__.copy()
        ans.update({'__class__': __class__.__name__})
        ans['created_at'] = ans['created_at'].isoformat()
        ans['updated_at'] = ans['updated_at'].isoformat()
        return ans

    def __str__(self):
        return "[BaseModel] ("+self.id+")"+str(self.__dict__)
