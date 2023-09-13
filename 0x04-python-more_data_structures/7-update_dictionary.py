#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
        upd_dictionary = dict(a_dictionary)
        if type(key) is str:
            upd_dictionary[key] = value
        return upd_dictionary
