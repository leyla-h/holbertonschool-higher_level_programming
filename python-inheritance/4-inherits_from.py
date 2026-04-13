#!/usr/bin/python3
"""
This module contains the function inherits_from.
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is a subclass instance; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
