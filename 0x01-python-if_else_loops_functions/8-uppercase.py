#!/usr/bin/python3

def uppercase(str):
    for ch in str:
        c = ord(ch)
        if c >= 97 and c <= 122:
            c -= 32
        print("{}".format(chr(c)), end="")
    else:
        print("")

