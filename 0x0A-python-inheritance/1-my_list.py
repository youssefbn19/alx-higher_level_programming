#!/usr/bin/python3
"""
The Module contains MyList class
check the class __doc__ for more details
"""


class MyList(list):
    """
    Simple class inherits from list
    """
    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        cpy = self.copy()
        cpy.sort()
        print(cpy)
