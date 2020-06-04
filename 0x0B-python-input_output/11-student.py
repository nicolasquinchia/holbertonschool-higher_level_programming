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

    def to_json(self):
        """Method to convert an obj to json(dict)

        Returns:
            [dict] -- all information as a dict
        """
        return self.__dict__
