#!/usr/bin/python3
def islower(c):
    if 'a' <= c <= 'z':
        return True
    elif 'A' <= c <= 'Z':
        return False
    elif not c:
        return True
    else:
        return False
