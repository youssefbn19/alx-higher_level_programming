#!/usr/bin/python3
"""
The Module contains only inherits_from() function
check the function __doc__ for more details
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the
    specified class. Otherwise False.
    """
    if type(obj) is a_class:
        return False
    else:
        return issubclass(type(obj), a_class)
