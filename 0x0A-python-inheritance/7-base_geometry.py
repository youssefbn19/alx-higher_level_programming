#!/usr/bin/python3
"""
The Module contains only BaseGeometry class
check the class __doc__ for more details
"""


class BaseGeometry:
    """
    Simple class with area and integer_validator funtions
    """
    def area(self):
        """
        The area function only raises an Exception with a message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value argument and raise an exception
        depends on the error that will occur
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
