#!/usr/bin/python3
""" Square class definition """


class Square:
    """ this class represents a square """
    def __init__(self, size):
        """ new square instance initialization with a size
        Args:
        - int size: size of the square. set to 0 """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
