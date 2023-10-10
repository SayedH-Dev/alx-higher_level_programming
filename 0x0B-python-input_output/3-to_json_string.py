#!/usr/bin/python3
""" defines a function that returns JSON representation of an object """
import json


def to_json_string(my_obj):
    """ a function that return JSON representation of an object
    Args:
        - my_obj: object to be converted to JSON
    Return: JSON representation of the object
    """
    return json.dumps(my_obj)
