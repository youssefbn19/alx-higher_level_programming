#!/usr/bin/python3
"""
The Module contains to_json_string function
check the function __doc__ for more details
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).
    """
    import json
    return json.dumps(my_obj)
