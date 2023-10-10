#!/usr/bin/python3
""" module that contains Student class """


class Student:
    """ defines a student """
    def __init__(self, first_name, last_name, age):
        """ function that initializes a Student instance
        with the corresponding arguments """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ function that retrives a dictionary
        represntation of Student instance
        Args:
            - list attrs: list of attributes to be retrived
            if None, retrive all attributes
        """
        if attrs is None:
            return self.__dict__
        result = {}
        for att in attrs:
            if hasattr(self, att):
                result[att] = getattr(self, att)
        return result

    def reload_from_json(self, json):
        """ function that replaces all the attributes in Student class
        with values from a dictionary
        Args:
            json: dictionary that has names and values
        """
        for key, value in json.item():
            setattr(self, key, value)
