#!/usr/bin/python3
"""
Module for Shape, Circle and Rectangle.
"""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract class for Shape."""

    @abstractmethod
    def area(self):
        """Method to calculate area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Method to calculate perimeter."""
        pass


class Circle(Shape):
    """Circle class."""

    def __init__(self, radius):
        """Init for Circle."""
        self.radius = radius

    def area(self):
        """Area of circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Perimeter of circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class."""

    def __init__(self, width, height):
        """Init for Rectangle."""
        self.width = width
        self.height = height

    def area(self):
        """Area of rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Perimeter of rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Function that prints shape info.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
