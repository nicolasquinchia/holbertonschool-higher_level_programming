#!/usr/bin/python3
def uppercase(str):
    tmp_str = ""
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            tmp_str = tmp_str + chr(ord(i) - 32)
        else:
            tmp_str = tmp_str + i
    print("{}".format(tmp_str))
