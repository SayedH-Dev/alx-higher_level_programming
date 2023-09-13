#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if type(key) is str:
        a_dictionary[key] = value
