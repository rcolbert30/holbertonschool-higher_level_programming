#!/usr/bin/python3
'''Rectangle Module'''
from models.base import Base


class Rectangle(Base):
    '''rectangle class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' instantation of width, height, x, y and id'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''width getter'''
        return(self.__width)

    @width.setter
    def width(self, value):
        '''width setter'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''height getter'''
        return (self.__width)

    @height.setter
    def height(self, value):
        ''' height setter'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        '''x getter'''
        return (self.__x)

    @x.setter
    def x(self, value):
        '''x setter '''
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        '''y getter'''
        return (self.__y)

    @x.setter
    def y(self, value):
        ''' y setter'''
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__y = value

    def area(self):
        '''area method'''
        return self.__width * self.__height

    def display(self):
        """display method"""
        for i in range(0, self.y):
            print()
        for i in range(0, self.height):
            for l in range(0, self.x):
                print(" ", end="")
            for l in range(0, self.width):
                print("#", end="")
            print()

    def __str__(self):
        '''returns string representation'''
        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format
                (self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        '''assigns argument to each attribute'''
        if len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''returns the dictionary representation of rectangle'''
        a_dict = {}
        a_dict["id"] = self.id
        a_dict["width"] = self.width
        a_dict["x"] = self.x
        a_dict["y"] = self.y
        return a_dict
