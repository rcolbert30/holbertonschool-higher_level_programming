#!/usr/bin/python3
class Student():

    def __init__(self, first_name="", last_name="", age=""):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__

    def to_json(self, attrs=None):
        if attrs is None:
            return (self.__dict__)
        return ({v: value for v, value in self.__dict__.items() if v in attrs})
