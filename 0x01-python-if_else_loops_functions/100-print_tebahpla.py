#!/usr/bin/python3
str1 = ""
for n in range(122, 96, -1):
    if n % 2 == 0:
        str1 = str1 + chr(n)
    else:
        str1 = str1 + chr(n - 32)
print("{}".format(str1), end='')
