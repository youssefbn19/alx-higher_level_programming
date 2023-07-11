#!/usr/bin/python3
"""
The Module contains MyList class
check the class __doc__ for more details
"""


class MyList(list):
    """
    Simple class inherits from list
    """
    def __init__(self):
        super().__init__(self)

    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
