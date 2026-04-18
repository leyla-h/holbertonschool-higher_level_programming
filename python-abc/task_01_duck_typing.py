#!/usr/bin/python3
"""
This module contains an abstract class Shape and its subclasses
Circle and Rectangle, demonstrating duck typing and inheritance.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for geometric shapes.
    """

    @abstractmethod
    def area(self):
        """
        Calculates the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculates the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Concrete class representing a circle, inheriting from Shape.
    """

    def __init__(self, radius):
        """
        Initializes a new Circle instance.
        Args:
            radius (int, float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Computes and returns the area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Computes and returns the perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Concrete class representing a rectangle, inheriting from Shape.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance.
        Args:
            width (int, float): The width of the rectangle.
            height (int, float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Computes and returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Computes and returns the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape using duck typing.
    Args:
        shape (Shape): An object that must implement area and perimeter.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
