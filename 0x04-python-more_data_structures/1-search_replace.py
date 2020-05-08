#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_str = []
    for x in my_list:
        if x == search:
            new_str.append(replace)
        else:
            new_str.append(x)
    return new_str
