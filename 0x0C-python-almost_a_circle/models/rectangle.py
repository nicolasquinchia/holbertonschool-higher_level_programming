#!/usr/bin/python3
"""This Module holds the class Rectangle
    """
from models.base import Base


class Rectangle(Base):
    """Rectangle class that defines a Rectangle

    Args:
        Base ([Class]): Class that init an object with
        an specific ID
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Construntor Method initilizator

        Args:
            width ([int]): width of the Rectangle
            height ([int]): height of the Rectangle
            x (int, optional): x distance. Defaults to 0.
            y (int, optional): y distance. Defaults to 0.
            id ([int], optional): Num that identify the obj. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """witdh getter

        Returns:
            [int]: Rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter

        Args:
            value ([obj]): Value to assign

        Raises:
            TypeError: width must be an integer
            ValueError: width must be > 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height getter

        Returns:
            [int]: Rectangle  height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter

        Args:
            value ([obj]): value to assign

        Raises:
            TypeError: height must be an integer
            ValueError: height must be > 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """x getter

        Returns:
            [int]: x value
        """
        return self.__x

    @x.setter
    def x(self, value):
        """x setter

        Args:
            value ([obj]): value to assign

        Raises:
            TypeError: x must be an integer
            ValueError: x must be >= 0
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """y getter

        Returns:
            [int]: y value
        """
        return self.__y

    @y.setter
    def y(self, value):
        """y setter

        Args:
            value ([obj]): value to assign

        Raises:
            TypeError: y must be an integer
            ValueError: y must be >= 0
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Method that return the rectangle area

        Returns:
            [int]: Area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """Method to print the rectangle with the
        # character
        """
        for y in range(self.y):
            print("")
        for i in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """Method that return the str representation

        Returns:
            [str]: Rectangle representation
        """
        p_id = str(self.id)
        p_w = str(self.width)
        p_h = str(self.height)
        p_x = str(self.x)
        p_y = str(self.y)
        str_to_prnt_1 = "[Rectangle] (" + p_id + ") " + p_x + "/" + p_y + " - "
        str_to_prnt = str_to_prnt_1 + p_w + "/" + p_h
        return str_to_prnt

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
                elif index == 2:
                    self.height = arg
                elif index == 3:
                    self.x = arg
                elif index == 4:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
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
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width,
        }
