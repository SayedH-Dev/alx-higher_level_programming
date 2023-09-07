#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1.py import add, sub, mul, div
    a = 10
    b = 5
    addition = add(a, b)
    subtraction = sub(a, b)
    multi = mul(a, b)
    division = div(a, b)
    print("{} + {} = {}".format(a, b, addition))
    print("{} - {} = {}".format(a, b, subtraction))
    print("{} * {} = {}".format(a, b, multi))
    print("{} / {} = {}".format(a, b, division))
