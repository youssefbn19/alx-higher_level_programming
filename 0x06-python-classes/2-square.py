#!/usr/bin/python3
""" Contains empty class called Square """


class Square:
    """ Square class that defines a square """
    def __init__(self, size=0):
        try:
            if size < 0:
                raise ValueError
            elif type(size) != int:
                raise TypeError
            self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
