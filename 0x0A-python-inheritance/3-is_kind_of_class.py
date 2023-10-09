#!/usr/bin/python3
""" defines a function that check a class and inherited class """


def is_kind_of_class(obj, a_class):
    """ a function that it checks if an object is instance of a class
    or of an inherited class from the specified class
    Args:
        - obj: object to be checked
        - a_class: the class to check for
    Return:
        - True if obj is an instance of a_class or its other inherited
        classes, False if not
    """
    return isinstance(obj, a_class)
