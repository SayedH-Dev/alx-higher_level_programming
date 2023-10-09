#!/usr/bin/python3
"""Defines Rectangle class that inherits from BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A class that represents a rectangle """

    def __init__(self, width, height):
        """ initializing a rectangle instance
        Args:
            - int width: rectangle width
            - int height: rectangle height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ function that calculates rectangle area """
        return self.__width * self.__height

    def __str__(self):
        """ magic method that returns a string representation of rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
