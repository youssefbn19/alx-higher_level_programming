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
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of a square
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a square description
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
