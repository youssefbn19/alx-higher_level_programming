#!/usr/bin/python3

def remove_char_at(str, n):
    copy = ""
    for index in range(0, len(str)):
        if index == n:
            continue
        copy += str[index]
    return copy
