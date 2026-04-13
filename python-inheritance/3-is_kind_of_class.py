#!/usr/bin/python3
"""
This module contains the function is_kind_of_class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or inherited from, a class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance or inherited; otherwise False.
    """
    return isinstance(obj, a_class)
