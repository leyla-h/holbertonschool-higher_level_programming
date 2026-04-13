#!/usr/bin/env python3
"""
Module for Abstract Base Classes and Duck Typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class for a shape."""

    @abstractmethod
    def area(self):
        """Calculates area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates perimeter."""
        pass


class Circle(Shape):
    """Circle class inheriting from Shape."""

    def __init__(self, radius):
        """Initialize with radius."""
        self.radius = radius

    def area(self):
        """Return circle area."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return circle perimeter."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class inheriting from Shape."""

    def __init__(self, width, height):
        """Initialize with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Return rectangle perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints area and perimeter using duck typing."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
