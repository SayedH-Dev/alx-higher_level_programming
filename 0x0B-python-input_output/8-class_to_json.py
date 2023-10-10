#!/usr/bin/python3
""" defines a class to JSON function """


def class_to_json(obj):
    """ function that converts a class instance to JSON serializable dictionary
    Args:
        - obj: an instance of a class to convert
    """
    return obj.__dict__
