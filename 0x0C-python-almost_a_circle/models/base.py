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

    @staticmethod
    def from_json_string(json_string):
        '''returns list of JSON string representation'''
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """dict to instance"""
        if dictionary is None:
            return
        if cls.__name__ == "Base":
            if "id" in dictionary.keys():
                return cls(dictionary["id"])
            else:
                return cls()
        else:
            retcls = cls(4, 4, 4)
            retcls.update(**dictionary)
            return retcls

    @classmethod
    def load_from_file(cls):
        '''loads from a file'''
        try:
            with open(cls.__name__ + ".json", "r") as f:
                j = cls.from_json_string(f.read())
            return [cls.create(**a) for a in j]
        except:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """load from csv file"""
        with open(cls.__name__ + ".csv") as f:
            lfg = []
            lob = []
            r = csv.DictReader(f)
            for l in r:
                lfg.append(l)
            for a in lfg:
                for key in l.keys():
                    l[key] = int(l[key])
            for c in lfg:
                lob.append(cls.create(**d))
            return lob
