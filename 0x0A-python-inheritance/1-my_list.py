#!/usr/bin/python3
""" defines a class that inherits from a list """


class MyList(list):
    """ class that inherits from list """

    def print_sorted(self):
        """ function that prints a list in an ascending order """
        print(sorted(self))
