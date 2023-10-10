#!/usr/bin/python3
""" defines a function that write to a text file """


def write_file(filename="", text=""):
    """ a function that writes to a UTF-8 text file and returns the number of
    the written charachters
    Args:
        - filename: the file to write in
        - text: the text to write into the file
    Return: no. of written charachters
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        written_char = file.write(text)
    return written_char
