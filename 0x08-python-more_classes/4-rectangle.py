#!/usr/bin/python3
class Rectangle():
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("heighy must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        s = ""
        new_s = ""
        if self.__width == 0 or self.__height == 0:
            return new_s
        else:
            for a in range(self.height):
                for b in range(self.width):
                    s += "#"
                new_s += s
                if a != self.height - 1:
                    new_s += "\n"
                s = ""
        return new_s

    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))
