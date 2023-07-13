#!/usr/bin/python3
"""
The Module contains class Student
"""


class Student:
    """
    class defines a student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of
        a Student instance
        """
        if attrs is not None and all(type(at) is str for at in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__
