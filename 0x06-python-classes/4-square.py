#!/usr/bin/python3
""" Square class definition """


class Square:
    """ this class represents a square """
    def __init__(self, size=0):
        """ new square instance initialization with a size
        Args:
        - int size: size of the square. set to 0 """
        self.__size = size

    @property
    def size(self):
        """ size attribute getter
        Return:
        - size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        """ size attribute setter
        Args:
        - int value: size of the square """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ function that calculates the area of a square
        Return:
        - area of the square """
        return self.__size ** 2
