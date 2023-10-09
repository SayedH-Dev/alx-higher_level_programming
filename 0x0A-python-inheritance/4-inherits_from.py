#!/usr/bin/python3
""" defines a function that checks an inherited class """


def inherits_from(obj, a_class):
    """ function that checks if an object is an instance of an inherited
    class from a specific class
    Args:
        - obj: object to be checked
        - a_class: the class to check for inherited class
        to check the object
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
