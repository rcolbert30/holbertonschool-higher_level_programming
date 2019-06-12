#!/usr/bin/python3
'''Base Module'''
import json
import csv


class Base():
    '''Base Module id assignment'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''intiate id'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' to json string'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file method"""
        if list_objs is None:
            with open(cls.__name__ + ".json", "w+") as f:
                f.write("[]")
        else:
            with open(cls.__name__ + ".json", "w+") as f:
                f.write(Base.to_json_string([x.to_dictionary()
                                            for x in list_objs]))
