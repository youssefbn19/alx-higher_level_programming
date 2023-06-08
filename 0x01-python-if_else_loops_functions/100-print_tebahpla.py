#!/usr/bin/python3

for char_code in range(122, 96, -1):
    if char_code % 2 == 1:
        char_code -= 32
    print("{}".format(chr(char_code)), end="")
