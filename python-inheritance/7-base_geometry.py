#!/usr/bin/python3
"""
This module defines a class BaseGeometry.
"""


class BaseGeometry:
    """A class with area and integer_validator methods."""

    def area(self):
        """Raises an Exception: area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value as a positive integer.

        Args:
            name (str): The name string.
            value (int): The value to check.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
