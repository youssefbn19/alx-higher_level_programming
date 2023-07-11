#!/usr/bin/python3
"""
The Module contains MyList class
"""


class MyList(list):
    """
    Simple class inherits from list
    """

    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
