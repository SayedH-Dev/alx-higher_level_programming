#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multi_dictionary = []
    for key, value in a_dictionary.items():
        multi_dictionary[key] = value * 2
    return multi_dictionary
