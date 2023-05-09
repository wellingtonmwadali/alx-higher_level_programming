#!/usr/bin/python3
l = 0
for n in range(122, 96, -1):
    print("{0}".format(chr(n - l)), end="")
    if l == 0:
        l = 32
    else:
        l = 0
