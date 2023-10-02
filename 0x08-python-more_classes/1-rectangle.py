#!/usr/bin/python3
""" Rectangle class definition """


class Rectangle:
    """class that represent a rectangle"""
    def __init__(self, width=0, height=0):
        """ rectangle initialization
        Args:
            - int width: rectangle width, default 0
            - int height: rectangle height, default 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter method for width """
        return self.width

    @width.setter
    def width(self, value):
        """ Setter method fot width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.width = value

    @property
    def height(self):
        """ Getter method for height """
        return self.height

    @height.setter
    def height(self, value):
        """ Setter method fot height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.height = value