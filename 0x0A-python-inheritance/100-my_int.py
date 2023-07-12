#!/usr/bin/python3
"""
The Module contains MyInt class
check the class  __doc__ for more details
"""


class MyInt(int):
    """
    The class MyInt that inherits from int
    """
    def __eq__(self, cmp_int):
        """
        Return False if two int are equal
        """
        return False

    def __ne__(self, cmp_int):
        """
        Return True if two int are not equal
        """
        return True
