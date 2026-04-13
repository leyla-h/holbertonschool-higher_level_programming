#!/usr/bin/python3
"""
This module defines an abstract class Shape and its subclasses
Circle and Rectangle, demonstrating ABCs and duck typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for all geometric shapes."""

    @abstractmethod
    def area(self):
        """Calculates and returns the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates and returns the perimeter of the shape."""
        pass


class Circle(Shape):
    """Concrete class representing a circle, inheriting from Shape."""

    def __init__(self, radius):
        """Initializes a Circle instance with a radius."""
        self.radius = radius

    def area(self):
        """Returns the area of the circle using math.pi."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Returns the perimeter of the circle using math.pi."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Concrete class representing a rectangle, inheriting from Shape."""

    def __init__(self, width, height):
        """Initializes a Rectangle instance with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape object.
    
    This function utilizes duck typing to call area() and perimeter()
    on the passed object without explicitly checking its type.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
