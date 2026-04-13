#!/usr/bin/python3
"""
Module for Shape, Circle, Rectangle classes and shape_info function.
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
        """Initialize Circle with radius."""
        self.radius = radius

    def area(self):
        """Calculate and return area of circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate and return perimeter of circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class that inherits from Shape."""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate and return area of rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return perimeter of rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape.
    Rely on duck typing to call area and perimeter methods.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
