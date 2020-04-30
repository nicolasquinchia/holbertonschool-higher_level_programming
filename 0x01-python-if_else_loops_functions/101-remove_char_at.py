#!/usr/bin/python3
def remove_char_at(str, n):
    idx = 0
    str1 = ""
    for i in str:
        if idx != n:
            str1 = str1 + i
        idx = idx + 1
    return str1
