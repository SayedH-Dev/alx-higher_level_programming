#!/usr/bin/python3
def uppercase(s):
    upper = ""
    for letter in s:
        if 'a' <= letter <= 'z':
            up_letter = chr(ord(letter) - 32)
            upper += up_letter
        else:
            upper += letter
    print("{}".format(upper))
