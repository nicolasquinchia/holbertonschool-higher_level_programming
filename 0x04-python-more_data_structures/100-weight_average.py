#!/usr/bin/python3
def weight_average(my_list=[]):
    i = 0
    j = 0
    if my_list:
        for n in my_list:
            j = j + n[0] * n[1]
            i = i + n[1]
        return j / i
    return 0
