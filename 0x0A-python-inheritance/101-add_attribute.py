#!/usr/bin/python3
"""
The Module contains only add_attribute() function
check the function __doc__ for more details
"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if it’s possible.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
