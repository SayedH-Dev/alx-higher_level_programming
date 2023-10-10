#!/usr/bin/python3
""" defines a function that saves an object to a text file in JSON format """
import json


def save_to_json_file(my_obj, filename):
    """ a function that saves an object to a text file
    using its JSON representation
    Args:
        - my_obj: the object to be saved
        - str filename: name of the text file to save the object in
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
