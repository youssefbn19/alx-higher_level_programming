#!/usr/bin/python3
"""
The Module contains save_to_json_file function
check the function __doc__ for more details
"""


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.
    """
    import json
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
