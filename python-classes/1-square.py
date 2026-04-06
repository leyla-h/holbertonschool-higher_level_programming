#!/usr/bin/python3
"""Module that defines a Square with a private size attribute"""


class Square:
    """Class representing a square"""

    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size: The size of the square's side.
        """
        self.__size = size
