#!/usr/bin/python3
""" rectangle class """
from models.base import Base


class Rectangle(Base):
    """ class that represents rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor method """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        """ getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        """ getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        """ getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter for x """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter for y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ return rectangle area """
        return self.__width * self.__height

    def display(self):
        """ display rectangle with handling x & y"""
        for i in range(self.__y):
            print()
        for j in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """ string representation of rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id,
                self.__x,
                self.__y,
                self.__width,
                self.__height)

    def update(self, *args, **kwargs):
        """ attributes update with arguments or keyworded arguments"""
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in ["id", "width", "height", "x", "y"]:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ return dictionary of Rectangle """
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}

    def to_csv_dict(self):
        """ converts object attributes to dictionary
        for CSV serialization """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y,
        }
