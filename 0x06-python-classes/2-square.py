#!/usr/bin/python3
""" Contains empty class called Square """


class Square:
    """ Square class that defines a square """
    def __init__(self, size=0):
        """ initialize the private field size
            set its value to 0 by default,
            check the size field type and value before assign it """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
