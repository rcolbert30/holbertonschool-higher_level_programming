#!/usr/bin/python3
class Square:
    __size = 0

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value > 0:
            self.__size - value
        else:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
