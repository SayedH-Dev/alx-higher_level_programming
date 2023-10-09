#!/usr/bin/python3
""" Defines an object lookup function """


def lookup(obj):
    """ A function that returns the list of available attributes
    and methods of an object.
    Args:
        - obj: object
    Return:
        - list of attributes and methods
    """
    return (dir(obj))
