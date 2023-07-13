#!/usr/bin/python3
"""
The Module contains write_file function
check the function __doc__ for more details
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and
    returns the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
