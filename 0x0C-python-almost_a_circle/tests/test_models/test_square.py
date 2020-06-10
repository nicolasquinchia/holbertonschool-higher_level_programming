#!/usr/bin/python3
"""This module holds the class for unit test
    teting the class Square
    """
import unittest
import os
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_square(unittest.TestCase):
    """Class with unitests for class Square

    Args:
        unittest ([class]): Class for unittest
    """

    def test_square_pep8(self):
        """Check PEP8 style
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0)


if __name__ == "__main__":
    unittest.main()
