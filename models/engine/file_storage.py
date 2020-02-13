#!/usr/bin/python3

import json
import os.path as path

"""
    bla bla bla
"""

class FileStorage():

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[str(obj.__class__) + obj.id] = obj

    def save(self):
        with open(self.__file_path, mode="w", encoding="UTF-8") as a:
            txt = json.dumps(self.__objects)
            a.write(txt)

    def reload(self):
        if (path.isfile(self.__file_path)):
            with open(self.__file_path, encoding="UTF-8") as a:
                txt = a.read()
            return json.loads(txt)
        return {}

    @objects.setter
    def objects(self, value={}):
        self.__objects = value
