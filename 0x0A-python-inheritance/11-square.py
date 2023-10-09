#!/usr/bin/python3
""" defines a Rectangle subclass which is Square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ a subclass that represents a square """
    def __init__(self, size):
        """ Initializing a square instance
        Args:
            - int size: square size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """ magic method that returns a string representation of square """
        return "[Square] {}/{}".format(self.__size, self.__size)
