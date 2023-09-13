#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for num in my_list:
        if type(num) is int and num not in new_list:
            new_list.append(num)
    total = sum(new_list)
    return total
