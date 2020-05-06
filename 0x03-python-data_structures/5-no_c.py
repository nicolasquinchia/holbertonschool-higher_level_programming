#!/usr/bin/env python3
def no_c(my_string):
    new = ""
    for x in my_string:
        if x != 'c' and x != 'C':
             new = new + x
    return new
