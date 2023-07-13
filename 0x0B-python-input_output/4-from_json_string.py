#!/usr/bin/python3
"""
The Module contains from_json_string function
check the function __doc__ for more details
"""


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented
    by a JSON string
    """
    import json
    return json.loads(my_str)
