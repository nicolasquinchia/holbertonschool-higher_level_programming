#!/usr/bin/python3
"""This module holds the class Square
    """
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that defines a Square

    Args:
        Rectangle ([class]): Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor Method initializator

        Args:
            size ([int]): Size of the square
            x (int, optional): x distance. Defaults to 0.
            y (int, optional): y distance. Defaults to 0.
            id ([type], optional): Num that identify the obj. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter

        Returns:
            [int]: size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """size setter

        Args:
            value ([obj]): value to assign
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Method that return the str representation

        Returns:
            [str]: Square representation
        """
        str_id = str(self.id)
        str_height = str(self.height)
        str_x = str(self.x)
        str_y = str(self.y)
        str_new = "[Square] (" + str_id + ") " + str_x + "/" + str_y + " - "
        str_new = str_new + str_height
        return str_new

    def update(self, *args, **kwargs):
        """Method that update an instance/object
        """
        if args:
            index = 0
            for index, arg in enumerate(args):
                if index == 0:
                    self.id = arg
                elif index == 1:
                    self.width = arg
                    self.height = arg
                elif index == 2:
                    self.x = arg
                elif index == 3:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
                self.height = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Public Method that gives the instance as a dict

        Returns:
            [dict]: instance representation
        """
        return {
            "id": self.id,
            "x": self.x,
            "size": self.width,
            "y": self.y,
        }
