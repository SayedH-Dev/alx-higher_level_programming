#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div_list = []
    if my_list:
        for i in my_list:
            div_list.append(i % 2 == 0)
        return div_list
