#!/usr/bin/python3

from models.base import Base

class Rectangle(Base):


    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an int")
        elif value < 0:
            raise ValueError("width must be greater than 0")
        else:
            self.__width = value

    @property
    def height(self):
        return (self.__width)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an int")
        elif value < 0:
            raise ValueError("height must be greater than 0")
        else:
            self.__height = value

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an int")
        elif value < 0:
            raise ValueError("x must be greater than 0")
        else:
            self.__x = value

    @property
    def y(self):
        return (self.__y)

    @x.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an int")
        elif value < 0:
            raise ValueError("x must be greater than 0")
        else:
            self.__y = value

