#!/usr/bin/python3
def uppercase(s):
    for  letter in s:
        if 'a' <= letter <= 'z':
            up_letter = chr(ord(letter) - 32)
            print(up_letter, end='')
        else:
            print(letter, end='')
