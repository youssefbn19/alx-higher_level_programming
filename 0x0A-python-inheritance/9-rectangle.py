#!/usr/bin/python3
"""
The Module contains Rectangle class
check the class __doc__ for more details
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Instantiation function with width and height
        """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Return area of a Rectangle instance
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a rectangle description
        """
        return "[{}] {}/{}".format(type(self).__name__,
                                   self.__width, self.__height)
