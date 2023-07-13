#!/usr/bin/python3
"""
The Module contains class_to_json function
check the function __doc__ for more details
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for
    JSON serialization of an object
    """
    return obj.__dict__
