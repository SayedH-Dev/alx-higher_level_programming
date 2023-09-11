#!/usr/bin/python3
def no_c(my_string):
    string_rep = ""
    for character in my_string:
        if character != 'c' and character != 'C':
            string_rep += character
    return string_rep
