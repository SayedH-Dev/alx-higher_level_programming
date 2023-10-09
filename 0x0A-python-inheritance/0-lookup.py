#!/usr/bin/python3
def lookup(obj):
    """ A function that returns the list of available attributes and methods of an object.
    Args:
        - obj: object
    Return:
        - list of attributes and methods
    """
    retrun [attribute for attribute in dir(obj) if not callable(getattr(obj, attribute))]
