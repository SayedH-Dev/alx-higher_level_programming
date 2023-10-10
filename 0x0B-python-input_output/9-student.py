#!/usr/bin/python3
""" module that contains Student class """


class Student:
    """ defines a student """
    def __init__(self, first_name, last_name, age):
        """ initializes a Student instance with the corresponding arguments """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ convert a class instance to JSON dictionary """
        return self.__dict__
