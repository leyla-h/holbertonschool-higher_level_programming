#!/usr/bin/env python3
"""
Module for documenting the use of Abstract Base Classes and Duck Typing.
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
    Circle class that inherits from Shape.
    """

    def __init__(self, radius):
        """Initializes the circle with a radius."""
        self.radius = radius

    def area(self):
        """Returns the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Returns the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle class that inherits from Shape.
    """

    def __init__(self, width, height):
        """Initializes the rectangle with width and height."""
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
    Function that prints the area and perimeter of a shape.
    Relying on duck typing, it calls area() and perimeter()
    without type checking.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
