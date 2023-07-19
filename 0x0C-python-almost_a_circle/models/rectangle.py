#!/usr/bin/python3
"""
The module contains a class named Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class instantiation function
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.attrValidation("width", width)
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.attrValidation("height", height)
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.attrValidation("x", x)
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.attrValidation("y", y)
        self.__y = y

    def attrValidation(self, attr, value):
        """
        Validation function for class attributes
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attr))
        elif attr in ["width", "height"]:
            if value <= 0:
                raise ValueError("{} must be > 0".format(attr))
        elif attr in ["x", "y"]:
            if value < 0:
                raise ValueError("{} must be >= 0".format(attr))

    def area(self):
        """
        Returns the area value of the Rectangle instance.
        """
        return self.width * self.height

    def display(self):
        """
        Prints in stdout the Rectangle instance with the character #.
        """
        for y in range(self.y):
            print()
        for h in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for w in range(self.width):
                print("#", end='')
            print()

    def __str__(self):
        """
        Custom string representation for instances of the class
        """
        return "[Rectangle] ({}) {}/{} - {}/{}"\
               .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute
        """
        if len(args) > 0:
            indx = 0
            for val in args:
                indx += 1
                if indx == 1:
                    self.id = val
                elif indx == 2:
                    self.width = val
                elif indx == 3:
                    self.height = val
                elif indx == 4:
                    self.x = val
                elif indx == 5:
                    self.y = val
                else:
                    break
        else:
            if kwargs is not None:
                for k, v in kwargs.items():
                    if hasattr(self, k):
                        setattr(self, k, v)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle
        """
        to_dict = {'id': self.id, 'width': self.width,
                   'height': self.height, 'x': self.x, 'y': self.y}
        return to_dict
