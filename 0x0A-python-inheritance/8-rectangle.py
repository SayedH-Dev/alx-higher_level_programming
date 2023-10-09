#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """A class that represents base geometry """

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ function that validates value and type integer
        Args:
            - str name: parameter name
            - int value: integer value
        Raises:
            - TypeError: if not integer
            - ValueError: if <= 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ A class that represents a rectangle """

    def __init__(self, width, height):
        """ initializing a rectangle instance
        Args:
            - int width: rectangle width
            - int height: rectangle height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
