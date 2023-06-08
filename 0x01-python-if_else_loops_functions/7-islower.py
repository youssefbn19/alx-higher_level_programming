#!/usr/bin/python3

def islower(c):
    check_char = ord(c)
    if check_char >= 97 and check_char <= 122:
        return True
    else:
        return False
