#!/usr/bin/python3
"""Module with LockedClass Class
"""


class LockedClass:
    """Prevents the user from dynamically
       creating new instance attributes
    """
    __slots__ = ['first_name']
