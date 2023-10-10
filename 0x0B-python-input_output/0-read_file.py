#!/usr/bin/python3
""" defines a function to read a text file """


def read_file(filename=""):
    """ function that read and print content of UTF-8 text file
    Args:
        - filename: name of the file to be read
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read(), end="")
