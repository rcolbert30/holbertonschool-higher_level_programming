#!/usr/bin/python3
class Square:
    __size = 0
    __position = 0

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value >= 0:
            self.__size = value
        else:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self.__position

    @size.setter
    def position(self, value):
        if (not isinstance(position, tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position > 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (not isinstance(position[0], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (not isinstance(postion[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for a in range(self.__position[0]):
                    print(" ", end="")
                for a in range(self.__size):
                    print("#", end="")
                print("")
