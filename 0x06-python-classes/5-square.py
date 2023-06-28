#!/usr/bin/python3
""" Contains empty class called Square """


class Square:
    """ Square class that defines a square """
    def __init__(self, size=0):
        """ initialize the private field size
            set its value to 0 by default,
            check the size field type and value before assign it """
        self.size = size

    @property
    def size(self):
        """ gets the private value size """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the private value size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Return the current square area"""
        return self.__size ** 2

    def my_print(self):
        """ prints in stdout the square with the character # """
        if self.size > 0:
            for i in range(0, self.size):
                for j in range(0, self.size):
                    print("#", end="")
                print()
        else:
            print()
