#!/usr/bin/python3
"""This Module contains Student class
    """


class Student:
    """Student Class define infomation about students
    """

    def __init__(self, first_name, last_name, age):
        """Contructor

        Arguments:
            first_name {[str]} -- First name of the stundent
            last_name {[str]} -- Last name of the stundent
            age {[int]} -- Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method to convert an obj to json(dict)

        Keyword Arguments:
            attrs {[list]} -- attrs to rtrn in dict (default: {None})

        Returns:
            [dict] -- all information as a dict
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dic = {}
            for attr_items in attrs:
                if attr_items in self.__dict__:
                    new_dic.update({attr_items: self.__dict__[attr_items]})
            return new_dic

    def reload_from_json(self, json):
        """ Method that replaces all attributes
        of the Student instance
        """
        for json_items in json:
            self.__dict__.update({json_items: json[json_items]})
