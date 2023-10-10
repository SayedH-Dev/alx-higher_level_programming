#!/usr/bin/python3
""" defines a function that parse a JSON string to Python data structure """
import json


def from_json_string(my_str):
    """ function that parses a JSON string into Python data structure
    Args:
        - str my_str: json string
    Return:
        - Python data structure
    """
    return json.loads(my_str)
