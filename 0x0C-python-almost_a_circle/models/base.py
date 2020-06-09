#!/usr/bin/python3
"""This module holds the class Base
    """
import json


class Base:
    """ Class that initialize an object with a
    specific id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor Method gives an ID

        Args:
            id ([int], optional): Uniq Num assing to the obj. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """dictionary to json string
        Arguments:
            list_dictionaries {[list]} -- list of dictionaries
        Returns:
            [str] -- json string representation of list_dictionaries
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """public Method that writes the JSON string
        representation of list_objs to a file:

        Args:
            list_objs ([list]): list of objects to
            represent as JSON and save on a file
        """
        if list_objs:
            n_list = [items.to_dictionary() for items in list_objs]
        else:
            n_list = []
        file_name = "{}.json".format(cls.__name__)
        with open(file_name, "w") as work_file:
            work_file.write(Base.to_json_string(n_list))

    @staticmethod
    def from_json_string(json_string):
        """Public method tha returns the list of
        the JSON string representation

        Args:
            json_string ([str]): json str that represents the obj

        Returns:
            [list]: decodification of the json string
        """
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Public method that returns an instance
        with all attributes set

        Returns:
            [obj]: Instance with all attributes
        """
        if cls.__name__ is "Rectangle":
            temp = cls(3, 1)
        else:
            temp = cls(6)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """Public method that creates intences from a json file

        Returns:
            [list]: list of all instances created
        """
        try:
            with open(cls.__name__ + ".json", "r") as work_file:
                return [
                    cls.create(**dic_new)
                    for dic_new in cls.from_json_string(work_file.read())
                ]
        except:
            return []
