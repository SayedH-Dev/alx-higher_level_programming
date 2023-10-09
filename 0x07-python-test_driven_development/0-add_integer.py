#!/usr/bin/python3
"""integer addition function"""


def add_integer(a, b=98):
    """
    function that adds 2 integers
    Para:
        a: integer or float
        b: integer or float and default 98
    Return:
        sum of a and b as integer
    """
    if a is None:
        raise TypeError("Both parameters should be either int or float")

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both parameters should be either int or float")
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    total = a + b
    return int(total)
