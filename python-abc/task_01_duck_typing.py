#!/usr/bin/python3
"""
This module defines an abstract class Shape and its subclasses
Circle and Rectangle, along with a function to display their info.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract class Shape that defines the blueprint for geometric shapes.
    """

    @abstractmethod
    def area(self):
        """Calculates the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates the perimeter of the shape."""
        pass


class Circle(Shape):
    """
    Class Circle that inherits from Shape.
    """

    def __init__(self, radius):
        """Initializes the circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculates and returns the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculates and returns the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Class Rectangle that inherits from Shape.
    """

    def __init__(self, width, height):
        """Initializes the rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape using duck typing.

    Args:
        shape: An object that is expected to have area() and perimeter()
               methods, regardless of its class inheritance.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
