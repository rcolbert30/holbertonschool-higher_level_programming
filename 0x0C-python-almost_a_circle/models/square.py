#!/usr/bin/python3
'''square module'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''square rectangle'''

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        '''string representation'''
        return "[Square] ({:d}) {:d}/{:d} - {:d}".\
            format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """update args"""
        if len(args) is not 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''returns dictionary representation of a Square'''
        a_dict = {}
        a_dict["id"] = self.id
        a_dict["size"] = self.size
        a_dict["x"] = self.x
        a_dict["y"] = self.y
        return a_dict
