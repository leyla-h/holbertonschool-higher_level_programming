#!/usr/bin/python3
"""
Module for Shape, Circle, Rectangle and shape_info function.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class Shape."""

    @abstractmethod
    def area(self):
        """Abstract method area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method perimeter."""
        pass


class Circle(Shape):
    """Circle class that inherits from Shape."""

    def __init__(self, radius):
        """Initializes Circle with radius."""
        self.__radius = radius

    def area(self):
        """Returns the area of the circle."""
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """Returns the perimeter of the circle."""
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """Rectangle class that inherits from Shape."""

    def __init__(self, width, height):
        """Initializes Rectangle with width and height."""
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height)


def shape_info(obj):
    """
    Prints the area and perimeter of an object using duck typing.
    """
    print("Area: {}".format(obj.area()))
    print("Perimeter: {}".format(obj.perimeter()))
