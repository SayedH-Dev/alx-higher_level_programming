#!/usr/bin/python3
""" defines a function to append a string to a text file """


def append_write(filename="", text=""):
    """ function that appends a string to a UTF-8 text file and returns
    the number of characters added
    Args:
        - filename: the file to append to
        - text: the text to append to the file
    Return: no. of added characters
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
