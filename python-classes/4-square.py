#!/usr/bin/python3
"""Module with a Square class using property getters and setters"""


class Square:
    """Class Square that defines a square"""

    def __init__(self, size=0):
        """Initialize the square with an optional size"""
        self.size = size

    @property
    def size(self):
        """Getter: retrieve the private size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter: set the private size attribute with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Public method that returns the current square area"""
        return self.__size ** 2
