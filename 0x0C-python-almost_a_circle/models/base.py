#!/usr/bin/python3
""" base class """
import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor method """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes JSON string representation of list_objs to a file """
        f = cls.__name__ + ".json"
        dicts = [obj.to_dictionary() for obj in list_objs]
        with open(f, mode='w', encoding='utf-8') as file:
            file.write(cls.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """ returns a list of dictionaries from JSON string """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ creates instance with attributes from a dictionary """
        dummy = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns instances list from JSON file """
        f = cls.__name__ + ".json"
        instance_list = []

        try:
            with open(f, mode='r', encoding='utf-8') as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                for dictionary in dictionaries:
                    instance = cls.create(**dictionary)
                    instance_list.append(instance)
        except FileNotFoundError:
            pass
        return instance_list
