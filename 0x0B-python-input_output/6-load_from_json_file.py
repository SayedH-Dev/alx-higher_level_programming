#!/usr/bin/python3
""" defines a function that creates an object from JSON file """
import json


def load_from_json_file(filename):
    """ a function that creates an object from a json file
    Args:
        - str filename: name of the json file
    Return:
        - Python object
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
