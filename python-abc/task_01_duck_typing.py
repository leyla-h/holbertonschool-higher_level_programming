#!/usr/bin/python3
"""
Module defining Shape abstract class and its subclasses Circle and Rectangle.
Uses ABCs to enforce method implementation and demonstrates Duck Typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for all shapes."""

    @abstractmethod
    def area(self):
        """Calculates the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates the perimeter of the shape."""
        pass


class Circle(Shape):
    """Concrete class representing a Circle."""

    def __init__(self, radius):
        """Initializes Circle with a private radius."""
        self.__radius = radius

    def area(self):
        """Returns the area of the circle using math.pi."""
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """Returns the perimeter of the circle using math.pi."""
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """Concrete class representing a Rectangle."""

    def __init__(self, width, height):
        """Initializes Rectangle with private width and height."""
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape object using duck typing.
    Does not perform isinstance checks.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
