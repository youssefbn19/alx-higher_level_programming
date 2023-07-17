#!/usr/bin/python3
"""
The module contains a class named Square
"""
from rectangle import Rectangle


class Square(Rectangle):
    """
    Class square inherits from Base
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class instantiation function
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        """
        Custom string representation for instances of the class Square
        """
        return "[square] ({}) {}/{} - {}"\
               .format(self.id, self.x, self.y, self.width)

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
                    self.size = val
                elif indx == 3:
                    self.x = val
                elif indx == 4:
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
        Returns the dictionary representation of a Square.
        """
        to_dict = {'id': self.id, 'size': self.size,
                   'x': self.x, 'y': self.y}
        return to_dict
