#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    mod_list = my_list[:idx] + my_list[idx + 1:]
    my_list[:] = mod_list
    return mod_list
