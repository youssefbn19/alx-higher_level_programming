#!/usr/bin/python3
"""
The Module contains a script that adds all arguments
to a Python list, and then save them to a file
"""


import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if not os.path.exists("add_item.json"):
    save_to_json_file([], "add_item.json")
else:
    py_list = load_from_json_file("add_item.json")
    py_list += sys.argv[1:]
    save_to_json_file(py_list, "add_item.json")
