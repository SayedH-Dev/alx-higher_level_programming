#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    my_list.sort()
    max_num = my_list[-1]
    print("{:d}".format(max_num))
