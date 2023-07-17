#!/usr/bin/python3
"""
The module contains class named Base
"""
import json


class Base:
    """
    The base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class instantiation function
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        elif type(list_dictionaries) is list:
            if len(list_dictionaries) == 0:
                return "[]"
            elif all(type(d) is dict for d in list_dictionaries):
                return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.
        """
        with open("{}.json".format(cls.__name__), "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                l_dic = [inst.to_dictionary() for inst in list_objs]
                f.write(cls.to_json_string(l_dic))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.
        """
        if cls.__name__ == "Square":
            instance = cls(1)
        else:
            instance = cls(1, 1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances:.
        """
        with open("{}.json".format(cls.__name__), encoding="utf-8") as f:
            list_inst = []
            if f is None:
                return list_inst
            else:
                list_inst = cls.from_json_string(f.read())
        return [cls.create(**inst) for inst in list_inst]
