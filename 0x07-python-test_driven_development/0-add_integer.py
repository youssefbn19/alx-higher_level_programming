#!/usr/bin/python3
"""
Module contains add_integer function for calculate
the addition of two number
"""


def add_integer(a, b=98):
    """ Returns the addition of a and b """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a + b)
