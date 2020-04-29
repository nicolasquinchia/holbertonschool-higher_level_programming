#!/usr/bin/python3
alpha = "abcdefghijklmnopqrstuvwxyz"
i = 0
while i <= 25:
    if alpha[i] != 'e' and alpha[i] != 'q':
        print('{}'.format(alpha[i]), end='')
    i = i + 1
