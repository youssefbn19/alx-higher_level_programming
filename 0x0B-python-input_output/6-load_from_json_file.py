#!/usr/bin/python3
"""
The Module contains load_from_json_file function
check the function __doc__ for more details
"""


def load_from_json_file(filename):
    """
    Create an Object from a “JSON file”
    """
    import json
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
