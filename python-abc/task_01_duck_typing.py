#!/usr/bin/python3
"""
This module contains the Shape abstract base class, its concrete
subclasses Circle and Rectangle, and the shape_info function.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for a shape.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter.
        """
        pass


class Circle(Shape):
    """
    Class representing a circle.
    """

    def __init__(self, radius):
        """
        Initializes a Circle instance.
        """
        self.radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculates and returns the perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Class representing a rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Uses duck typing to print the area and perimeter of a shape.
    Args:
        shape: An object that has area() and perimeter() methods.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
