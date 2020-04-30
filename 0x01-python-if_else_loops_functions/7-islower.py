#!/usr/bin/python3
def islower(c):
    as_code = ord(c)
    if as_code > 96 and as_code < 123:
        return True
    else:
        return False
