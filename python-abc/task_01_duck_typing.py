#!/usr/bin/python3
"""
Module defining the Shape abstract class and its subclasses.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for geometric shapes.
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
    Concrete class representing a circle.
    """
    def __init__(self, radius):
        """Initialize circle with radius."""
        self.radius = radius

    def area(self):
        """Return area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Concrete class representing a rectangle.
    """
    def __init__(self, width, height):
        """Initialize rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape using duck typing.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
