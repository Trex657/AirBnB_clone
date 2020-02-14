#!/usr/bin/python3

import json
import os.path as path
from datetime import datetime
from models.base_model import BaseModel
import models

"""
    bla bla bla
"""

class FileStorage:

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        #key = obj['__class__'] + "." + obj['id']
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, mode="w", encoding="UTF-8") as a:
            new = {}
            for key, value in self.__objects.items():
                new[key] = value.to_dict()
            txt = json.dumps(new)
            a.write(txt)

    def reload(self):
        if (path.isfile(self.__file_path)):
            with open(self.__file_path, encoding="UTF-8") as a:
                txt = a.read()
            if(len(txt) > 0):
                dic = json.loads(txt)
                for key, value in dic.items():
                    obj = BaseModel(**value)
                    self.__objects[key] =  obj
