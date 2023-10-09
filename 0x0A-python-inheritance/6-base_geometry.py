#!/usr/bin/python3
""" defines a base class """


class BaseGeometry:
    """ base class for geometry """

    def area(self):
        raise Exception("area() is not implemented")
