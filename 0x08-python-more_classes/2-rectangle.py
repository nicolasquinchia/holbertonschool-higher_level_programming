#!/usr/bin/python3
"""Module with Rectangle class
"""


class Rectangle:
    """Class that defines a rectangle
           Properties : width, height
           Methods: Area, Perimeter
    """

    def __init__(self, width=0, height=0):
        """Initializer

                Keyword Arguments:
                        width {int} -- rectangle width (default: {0})
                        height {int} -- rectangle height (default: {0})
                """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width value Getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter

        Arguments:
                value {[int]} -- Rectangle width

        Raises:
                TypeError: width must be an integer
                ValueError: width must be >= 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter

        Arguments:
                value {[int]} -- Rectangle height

        Raises:
                TypeError: height must be an integer
                ValueError: height must be >= 0
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the rectangle area

        Returns:
            [int] -- Rectangle area
        """
        return (self.width * self.height)

    def perimeter(self):
        """Returns the rectangle perimeter

        Returns:
            [int] -- Rectangle perimeter
        """
        return ((self.width + self.height) * 2)
