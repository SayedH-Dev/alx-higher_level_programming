#!/usr/bin/python3
""" module with a function to append a line of text after specific lines """


def append_after(filename="", search_string="", new_string=""):
    """ function that append a line of text
    after each line that contains a specific string
    Args:
        - str filename: the name of the required file
        - str search_string: the string to search for in each line
        - str new_string: the line of text to be inserted
    """
    with open(filename, 'r') as file:
        read_lines = file.readlines()

    with open(filename, 'w') as file:
        for line in read_lines:
            file.write(line)
            if search_string not in line:
                file.write(new_string)
