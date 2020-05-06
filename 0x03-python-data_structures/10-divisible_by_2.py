#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_str = ""
    for x in my_list:
        if x % 2 == 0:
            new_str.append(True)
        else:
            new_str.append(False)
        return new_str
