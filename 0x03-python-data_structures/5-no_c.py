#!/usr/bin/env python3
def no_c(my_string):
    new_str = ""
    for x in my_string:
        if x != 'c' and x != 'C':
            new_str = new_str + x
    return new_str
