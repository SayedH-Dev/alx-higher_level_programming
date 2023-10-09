#!/usr/bin/python3
""" defines a function that checks a class """


def is_same_class(obj, a_class):
    """ function that checks if an object is an instnace of a class
    Args:
        - obj: object to be checked
        - a_class: the class to check for the object in.
    Return:
        - True if the object is instance of the class, False if not
    """
    return type(obj) is a_class
