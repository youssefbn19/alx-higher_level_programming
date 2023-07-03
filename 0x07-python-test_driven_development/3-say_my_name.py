#!/usr/bin/python3
"""
Module contains say_my_name function that
prints a sentence
"""


def say_my_name(first_name, last_name=""):
    """
    The function that prints My name is <first name> <last name>
    """
    if type(first_name) is not str:
       raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
       raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
