#!/usr/bin/python3
class Rectangle():
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            self.__width = value
        else:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            self.__height = value
        else:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("heighy must be >= 0")

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__height + self.__width))

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
                if a != self.__height - 1:
                    new_s += "\n"
                s = ""
        return new_s

    def __repr__(self):
        return ("Rectangle({:d} , {:d})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
