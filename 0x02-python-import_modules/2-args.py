#!/usr/bin/python3
from sys import argv
if len(argv) == 1:
    print("0 arguments.")
elif len(argv) == 2:
    print("1 argument:")
    print("1: {:s}".format(argv[1]))
else:
    print("{} arguments:".format((len(argv) - 1)))
    i = 1
    for j in argv[1:]:
        print("{:d}: {:s}".format(i, j))
        i += 1
