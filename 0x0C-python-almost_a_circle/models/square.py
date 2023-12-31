#!/usr/bin/python3
""" defines Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class that represents a square """

    def __init__(self, size, x=0, y=0, id=None):
        """ constructor method """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def __str__(self):
        """ string representation of Square """
        return "[Square] ({}) {}/{} - {}".format(
                self.id,
                self.x,
                self.y,
                self.width)

    def update(self, *args, **kwargs):
        """ update attributes on arguments and key worded arguments """
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in ['id', 'size', 'x', 'y']:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ return dictionary of Square """
        return {
                'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y}

    def to_csv_dict(self):
        """ convert sqaure attributes to a dictionary
        for CSV serialization """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y} 
