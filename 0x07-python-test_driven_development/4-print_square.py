#!/usr/bin/python3
"""
Module contains print_square function that
prints a square with character #
"""


def print_square(size):
    """
    The function that prints a square with
    the character #
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
