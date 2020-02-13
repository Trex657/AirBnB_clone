#!/usr/bin/python3

from datetime import datetime
import uuid

"""
    Class base for the others classes
"""


class BaseModel():

    def __init__(self, *args, **kwargs):
        if (len(kwargs) > 0):
            self.id = kwargs['id']
            self.name = kwargs['name']
            self.my_number = kwargs['my_number']
            self.created_at = datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        ans = "["
        ans += __class__.__name__
        ans += "] ("
        ans += self.id
        ans += ") "
        ans += str(self.__dict__)
        return ans

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        ans = self.__dict__
        ans.update({'__class__': __class__.__name__})
        ans['created_at'] = ans['created_at'].isoformat()
        ans['updated_at'] = ans['updated_at'].isoformat()
        return ans
