#!/usr/bin/python3
"""
The Module contains Sqaure class
check the class __doc__ for more details
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle
    """
    def __init__(self, size):
        """
        Instantiation function with size
        """
        super().__init__(size, size)
